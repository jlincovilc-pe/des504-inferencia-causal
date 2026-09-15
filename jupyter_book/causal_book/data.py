"""Capa de datos local y portátil."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Tuple

import pandas as pd

_PACKAGE_ROOT = Path(__file__).resolve().parent.parent


def project_root() -> Path:
    return _PACKAGE_ROOT


def data_dir() -> Path:
    env = os.environ.get("CAUSAL_BOOK_DATA")
    if env:
        p = Path(env).expanduser().resolve()
        if p.exists():
            return p
    for candidate in (
        _PACKAGE_ROOT / "data",
        _PACKAGE_ROOT / "datos",
        _PACKAGE_ROOT / "content" / "datos",
    ):
        if candidate.exists():
            return candidate.resolve()
    raise FileNotFoundError(
        "No se encontró la capa de datos. Ejecuta: python scripts/setup_local_data.py"
    )


def load_dataset(
    name: str,
    *,
    kind: Optional[str] = None,
    with_truth: bool = False,
) -> pd.DataFrame | Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Carga un dataset por nombre lógico.

    Ejemplos:
        load_dataset("nhefs")
        load_dataset("nsw_mixtape")
        load_dataset("mediation_post_treatment", kind="synthetic", with_truth=True)
        load_dataset("matching_hidden_confounder", with_truth=True)
    """
    root = data_dir()

    real_path = root / "real" / name / "data.csv"
    if real_path.exists() and kind in (None, "real"):
        df = pd.read_csv(real_path)
        return df

    # synthetic: search by leaf folder name
    synthetic_root = root / "synthetic"
    matches = list(synthetic_root.rglob(name)) if synthetic_root.exists() else []
    # also allow full relative path like "mediation/mediation_post_treatment"
    if not matches and (synthetic_root / name).exists():
        matches = [synthetic_root / name]
    folder = None
    for m in matches:
        if m.is_dir() and (m / "student.csv").exists():
            folder = m
            break
        if m.is_file() and m.name == "student.csv":
            folder = m.parent
            break
    if folder is None:
        # try direct path patterns used by notebooks
        candidates = [
            root / "synthetic" / name / "student.csv",
            *list(synthetic_root.glob(f"*/{name}/student.csv")),
            *list(synthetic_root.glob(f"*/*/{name}/student.csv")),
        ]
        for c in candidates:
            if c.exists():
                folder = c.parent
                break

    if folder is None:
        available_real = sorted(p.parent.name for p in (root / "real").glob("*/data.csv"))
        available_syn = sorted(
            p.parent.name for p in (root / "synthetic").rglob("student.csv")
        )
        raise FileNotFoundError(
            f"Dataset '{name}' no encontrado.\n"
            f"  reales: {available_real}\n"
            f"  sintéticos: {available_syn}"
        )

    student = pd.read_csv(folder / "student.csv")
    if with_truth:
        truth = pd.read_csv(folder / "truth_instructor_only.csv")
        return student, truth
    return student
