#!/usr/bin/env python3
"""
Reconstruye la capa de datos local del Jupyter Book de Inferencia Causal.

El paquete en la nube llegó con data/ incompleta (archivos sueltos y synthetic vacío)
mientras los notebooks esperan:

  datos/real/<dataset>/data.csv
  datos/synthetic/<familia>/<nombre>/{student,truth_instructor_only}.csv

Este script:
  1. Descarga datasets reales públicos (causaldata vía Rdatasets)
  2. Genera datasets sintéticos con seed fija y ground truth
  3. Escribe en data/ (canónico) y content/datos -> enlace a data/

Uso:
  python scripts/setup_local_data.py
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SEED = 42
BASE = "https://vincentarelbundock.github.io/Rdatasets/csv/causaldata"


def ensure_dir(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


def write_csv(df: pd.DataFrame, path: Path) -> None:
    ensure_dir(path.parent)
    df.to_csv(path, index=False)
    print(f"  ✓ {path.relative_to(ROOT)}  ({len(df)} filas, {df.shape[1]} cols)")


def download_real(*, force: bool = False) -> None:
    """Descarga reales solo si faltan (modo offline: reutiliza data/ en disco local)."""
    print("\n=== Datasets reales (disco local) ===")
    mapping = {
        "nsw_mixtape": f"{BASE}/nsw_mixtape.csv",
        "nhefs": f"{BASE}/nhefs.csv",
        "close_college": f"{BASE}/close_college.csv",
        "texas": f"{BASE}/texas.csv",
        "thornton_hiv": f"{BASE}/thornton_hiv.csv",
        "mortgages": f"{BASE}/mortgages.csv",
    }
    for name, url in mapping.items():
        dest = DATA / "real" / name / "data.csv"
        if dest.exists() and dest.stat().st_size > 0 and not force:
            print(f"  · {name} (ya en SSD local: {dest.relative_to(ROOT)})")
            continue
        print(f"  ↓ {name}  ← red (solo primera vez)")
        df = pd.read_csv(url)
        if "rownames" in df.columns:
            df = df.drop(columns=["rownames"])
        if name == "mortgages":
            # El notebook usa un subconjunto manejable (~1000 obs)
            df = df.sample(n=min(1000, len(df)), random_state=SEED).reset_index(drop=True)
            # Cap. 31 usa bpl como covariable numérica (RF/OLS); codificar estado de nacimiento
            # pandas 3 puede reportar dtype "str" (no object)
            if not pd.api.types.is_numeric_dtype(df["bpl"]):
                df["bpl"] = pd.Categorical(df["bpl"]).codes.astype(int)
        write_csv(df, dest)


def gen_mediation(n: int = 3500) -> None:
    rng = np.random.default_rng(SEED)
    # DGP (Cap. 1, 10, 13): X → M → Y y X → Y
    # X ~ Bern(0.5); M := 0.5 + 1.2 X + U_m; Y := 1.0 + 0.8 X + 1.0 M + U_y
    x_baseline = rng.normal(0, 1, n)
    treatment = rng.binomial(1, 0.5, n)
    u_m = rng.normal(0, 1, n)
    u_y = rng.normal(0, 1, n)
    direct = 0.8
    a = 1.2  # X→M
    b = 1.0  # M→Y
    mediator0 = 0.5 + 0.0 * treatment + 0.3 * x_baseline + u_m  # under X=0 style base
    mediator = 0.5 + a * treatment + 0.3 * x_baseline + u_m
    y0 = 1.0 + direct * 0 + b * (0.5 + 0.3 * x_baseline + u_m) + 0.2 * x_baseline + u_y
    y1 = 1.0 + direct * 1 + b * (0.5 + a + 0.3 * x_baseline + u_m) + 0.2 * x_baseline + u_y
    y_outcome = 1.0 + direct * treatment + b * mediator + 0.2 * x_baseline + u_y
    student = pd.DataFrame(
        {
            "id": np.arange(1, n + 1),
            "treatment": treatment,
            "x_baseline": x_baseline,
            "mediator": mediator,
            "y_outcome": y_outcome,
        }
    )
    truth = pd.DataFrame(
        {
            "id": np.arange(1, n + 1),
            "direct_effect_truth": np.full(n, direct),
            "indirect_effect_truth": np.full(n, a * b),
            "total_effect_truth": np.full(n, direct + a * b),
            "mediator0_truth": mediator0,
            "mediator_observed_truth": mediator,
            "y0_truth": y0,
            "y1_truth": y1,
        }
    )
    base = DATA / "synthetic" / "mediation" / "mediation_post_treatment"
    write_csv(student, base / "student.csv")
    write_csv(truth, base / "truth_instructor_only.csv")


def gen_matching_hidden(n: int = 2000) -> None:
    rng = np.random.default_rng(SEED + 1)
    x1 = rng.normal(0, 1, n)
    x2 = rng.normal(0, 1, n)
    u = rng.normal(0, 1, n)  # confusor oculto
    # propensity depends on x1,x2 and u
    logits = -0.3 + 0.8 * x1 - 0.5 * x2 + 1.2 * u
    e = 1 / (1 + np.exp(-logits))
    d = rng.binomial(1, e)
    true_tau = 1.0
    y0 = 1.0 + 0.5 * x1 + 0.3 * x2 + 1.5 * u + rng.normal(0, 1, n)
    y1 = y0 + true_tau
    y = np.where(d == 1, y1, y0)
    student = pd.DataFrame({"x1": x1, "x2": x2, "d_treated": d, "y_outcome": y})
    truth = pd.DataFrame(
        {
            "true_tau": np.full(n, true_tau),
            "propensity_truth": e,
            "u_hidden_truth": u,
            "y0_truth": y0,
            "y1_truth": y1,
        }
    )
    base = DATA / "synthetic" / "matching" / "matching_hidden_confounder"
    write_csv(student, base / "student.csv")
    write_csv(truth, base / "truth_instructor_only.csv")


def gen_iv_noncompliance(n: int = 3000) -> None:
    rng = np.random.default_rng(SEED + 2)
    x_baseline = rng.normal(0, 1, n)
    u = rng.normal(0, 1, n)
    z = rng.binomial(1, 0.5, n)
    # types: always, never, complier (no defiers by monotonicity)
    type_draw = rng.random(n)
    # ~20% always, 20% never, 60% complier
    compliance = np.where(
        type_draw < 0.20,
        "always_taker",
        np.where(type_draw < 0.40, "never_taker", "complier"),
    )
    d = np.zeros(n, dtype=int)
    d[compliance == "always_taker"] = 1
    d[compliance == "never_taker"] = 0
    d[compliance == "complier"] = z[compliance == "complier"]
    true_tau = np.where(compliance == "complier", 2.0, 0.5)
    y0 = 1.0 + 0.4 * x_baseline + 1.0 * u + rng.normal(0, 1, n)
    y1 = y0 + true_tau
    y = np.where(d == 1, y1, y0)
    student = pd.DataFrame(
        {
            "z_encouragement": z,
            "d_treated": d,
            "x_baseline": x_baseline,
            "y_outcome": y,
        }
    )
    truth = pd.DataFrame(
        {
            "compliance_type_truth": compliance,
            "true_tau": true_tau,
            "u_unobserved_truth": u,
            "y0_truth": y0,
            "y1_truth": y1,
        }
    )
    base = DATA / "synthetic" / "iv" / "iv_noncompliance"
    write_csv(student, base / "student.csv")
    write_csv(truth, base / "truth_instructor_only.csv")


def gen_iv_invalid_exclusion(n: int = 2500) -> None:
    rng = np.random.default_rng(SEED + 3)
    z = rng.binomial(1, 0.5, n)
    u = rng.normal(0, 1, n)
    d = (0.3 + 0.5 * z + 0.4 * u + rng.normal(0, 0.3, n) > 0.5).astype(int)
    true_tau = 1.0
    direct_z = 0.8  # exclusión VIOLADA
    y0 = 0.5 + direct_z * z + 1.0 * u + rng.normal(0, 1, n)
    y1 = y0 + true_tau
    y = np.where(d == 1, y1, y0)
    student = pd.DataFrame({"z_instrument": z, "d_treated": d, "y_outcome": y})
    truth = pd.DataFrame(
        {
            "true_tau": np.full(n, true_tau),
            "direct_effect_z_truth": np.full(n, direct_z),
            "exclusion_holds_truth": np.full(n, False),
            "u_unobserved_truth": u,
        }
    )
    base = DATA / "synthetic" / "iv" / "iv_invalid_exclusion"
    write_csv(student, base / "student.csv")
    write_csv(truth, base / "truth_instructor_only.csv")


def gen_rdd(n: int = 2000) -> None:
    rng = np.random.default_rng(SEED + 4)
    cutoff = 0.0
    true_tau = 2.0
    running = rng.uniform(-1, 1, n)
    above = (running >= cutoff).astype(int)
    y0 = 1.0 + 0.8 * running + rng.normal(0, 0.5, n)
    y = y0 + true_tau * above
    student = pd.DataFrame(
        {
            "running": running,
            "above_cutoff": above,
            "y_outcome": y,
        }
    )
    truth = pd.DataFrame(
        {
            "cutoff": np.full(n, cutoff),
            "true_tau_at_cutoff": np.full(n, true_tau),
            "y0_truth": y0,
        }
    )
    base = DATA / "synthetic" / "rdd" / "rdd_sharp_bandwidth"
    write_csv(student, base / "student.csv")
    write_csv(truth, base / "truth_instructor_only.csv")


def _gen_did(path_name: str, parallel: bool, n_units: int = 100, n_times: int = 10) -> None:
    rng = np.random.default_rng(SEED + (5 if parallel else 6))
    treat_start = 5
    true_att = 1.5
    rows = []
    truth_rows = []
    for i in range(1, n_units + 1):
        g = 1 if i <= n_units // 2 else 0
        alpha = rng.normal(0, 1)
        # parallel ok: same slope; violation: treated have different slope
        slope = 0.2 if parallel else (0.2 + 0.15 * g)
        for t in range(n_times):
            post = int(t >= treat_start)
            treated = int(g == 1 and post == 1)
            y0 = alpha + slope * t + rng.normal(0, 0.3)
            y = y0 + true_att * treated
            rows.append(
                {
                    "unit_id": i,
                    "time": t,
                    "treated_group": g,
                    "post": post,
                    "treated": treated,
                    "y_outcome": y,
                }
            )
            truth_rows.append(
                {
                    "unit_id": i,
                    "time": t,
                    "y0_truth": y0,
                    "true_ATT_post": true_att,
                    "parallel_trends_holds_truth": parallel,
                }
            )
    student = pd.DataFrame(rows)
    truth = pd.DataFrame(truth_rows)
    base = DATA / "synthetic" / "did" / path_name
    write_csv(student, base / "student.csv")
    write_csv(truth, base / "truth_instructor_only.csv")


def gen_rct_attrition(n: int = 2000) -> None:
    rng = np.random.default_rng(SEED + 7)
    true_tau = 1.0
    x = rng.normal(0, 1, n)
    treatment = rng.binomial(1, 0.5, n)
    y0 = 0.5 + 0.5 * x + rng.normal(0, 1, n)
    y1 = y0 + true_tau
    y_full = np.where(treatment == 1, y1, y0)
    # attrition depends on outcome (MNAR) → complete-case bias
    p_obs = 1 / (1 + np.exp(-(0.5 - 0.8 * y_full)))
    observed = rng.binomial(1, p_obs)
    observed_outcome = np.where(observed == 1, y_full, np.nan)
    student = pd.DataFrame(
        {
            "treatment": treatment,
            "x_baseline": x,
            "y_outcome": observed_outcome,
            "observed_outcome": observed_outcome,
        }
    )
    truth = pd.DataFrame(
        {
            "true_tau": np.full(n, true_tau),
            "y0_truth": y0,
            "y1_truth": y1,
            "y_full_truth": y_full,
            "p_observed_truth": p_obs,
        }
    )
    base = DATA / "synthetic" / "rct" / "rct_attrition"
    write_csv(student, base / "student.csv")
    write_csv(truth, base / "truth_instructor_only.csv")


def gen_panel_fe_dynamic(n_units: int = 60, n_times: int = 60) -> None:
    rng = np.random.default_rng(SEED + 8)
    treat_start = 30
    rows = []
    truth_rows = []
    for i in range(1, n_units + 1):
        g = 1 if i <= n_units // 2 else 0
        alpha = rng.normal(0, 1)
        slope = rng.normal(0.05 if g == 0 else 0.12, 0.02)  # heterogéneo → TWFE falla
        tau_i = 1.0 + 0.3 * g + rng.normal(0, 0.1)
        for t in range(n_times):
            treated = int(g == 1 and t >= treat_start)
            y0 = alpha + slope * t + rng.normal(0, 0.4)
            y = y0 + tau_i * treated
            rows.append(
                {
                    "unit_id": i,
                    "time": t,
                    "treated_group": g,
                    "treated": treated,
                    "y_outcome": y,
                }
            )
            truth_rows.append(
                {
                    "unit_id": i,
                    "time": t,
                    "unit_slope_truth": slope,
                    "y0_truth": y0,
                    "tau_i_truth": tau_i,
                    "tau_observed_truth": tau_i * treated,
                }
            )
    student = pd.DataFrame(rows)
    truth = pd.DataFrame(truth_rows)
    base = DATA / "synthetic" / "panel" / "panel_fe_dynamic"
    write_csv(student, base / "student.csv")
    write_csv(truth, base / "truth_instructor_only.csv")


def link_datos() -> None:
    """Enlaces relativos dentro del proyecto (todo en el SSD local)."""
    target = ROOT / "content" / "datos"
    if target.is_symlink() or target.exists():
        if target.is_symlink():
            target.unlink()
        elif target.is_dir():
            shutil.rmtree(target)
    try:
        target.symlink_to(Path("../data"), target_is_directory=True)
        print(f"\n  ✓ symlink content/datos -> ../data")
    except OSError:
        shutil.copytree(DATA, target, dirs_exist_ok=True)
        print(f"\n  ✓ copia content/datos (sin symlink)")

    root_datos = ROOT / "datos"
    if root_datos.is_symlink():
        root_datos.unlink()
    elif root_datos.exists():
        shutil.rmtree(root_datos)
    try:
        root_datos.symlink_to(Path("data"), target_is_directory=True)
        print(f"  ✓ symlink datos -> data")
    except OSError:
        pass


def write_manifest() -> None:
    real_files = sorted((DATA / "real").glob("*/data.csv"))
    syn_files = sorted((DATA / "synthetic").rglob("student.csv"))
    total_bytes = sum(p.stat().st_size for p in real_files) + sum(
        p.stat().st_size for p in (DATA / "synthetic").rglob("*.csv")
    )
    manifest = {
        "version": "1.1-local",
        "storage": "local-ssd",
        "root": str(ROOT),
        "data_dir": str(DATA),
        "seed": SEED,
        "offline_ready": all(p.exists() and p.stat().st_size > 0 for p in real_files)
        and len(syn_files) >= 9,
        "bytes_data_approx": total_bytes,
        "real": [p.parent.name for p in real_files],
        "synthetic": [
            str(p.relative_to(DATA / "synthetic").parent) for p in syn_files
        ],
        "notes": "Todo el material del libro vive en disco local (Mac SSD). "
        "No se requiere red para ejecutar notebooks si data/ está completa.",
    }
    ensure_dir(DATA / "manifests")
    path = DATA / "manifests" / "local_setup.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  ✓ {path.relative_to(ROOT)}")
    return manifest


def main() -> int:
    force = "--force" in sys.argv
    print(f"ROOT (SSD local): {ROOT}")
    ensure_dir(DATA / "real")
    ensure_dir(DATA / "synthetic")
    download_real(force=force)
    print("\n=== Datasets sintéticos (seed={}, escritos en disco) ===".format(SEED))
    gen_mediation()
    gen_matching_hidden()
    gen_iv_noncompliance()
    gen_iv_invalid_exclusion()
    gen_rdd()
    _gen_did("did_parallel_ok", parallel=True)
    _gen_did("did_parallel_violation", parallel=False)
    gen_rct_attrition()
    gen_panel_fe_dynamic()
    link_datos()
    manifest = write_manifest()
    # Forzar flush a disco
    for p in DATA.rglob("*"):
        if p.is_file():
            with open(p, "rb") as f:
                os = __import__("os")
                os.fsync(f.fileno())
    print("\n✓ Libro y datos guardados en el SSD local.")
    print(f"  Ruta: {ROOT}")
    print(f"  Offline ready: {manifest.get('offline_ready')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
