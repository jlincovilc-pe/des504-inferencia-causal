#!/usr/bin/env python3
"""Smoke test local: carga de datos + ejecución de celdas clave de 4 notebooks (uno por bloque)."""
from __future__ import annotations

import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import nbformat
from nbclient import NotebookClient


def test_data_layer() -> None:
    from causal_book.data import data_dir, load_dataset

    d = data_dir()
    print(f"data_dir = {d}")
    assert (d / "real" / "nsw_mixtape" / "data.csv").exists()
    assert (d / "real" / "nhefs" / "data.csv").exists()
    df = load_dataset("nsw_mixtape")
    assert "treat" in df.columns and "re78" in df.columns
    student, truth = load_dataset("mediation_post_treatment", with_truth=True)
    assert "treatment" in student.columns
    assert "total_effect_truth" in truth.columns
    print(f"  ✓ nsw_mixtape n={len(df)}; mediation n={len(student)}")


def run_notebook(path: Path, timeout: int = 180) -> None:
    print(f"\n→ Ejecutando {path.relative_to(ROOT)} ...")
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
    )
    # Allow matplotlib headless
    client.execute()
    print(f"  ✓ OK {path.name}")


def main() -> int:
    print("=== Smoke test local ===")
    test_data_layer()

    test_notebooks = [
        ROOT / "content/bloque_01_fundamentacion/01_paradoja_efecto_cero.ipynb",      # Bloque I
        ROOT / "content/bloque_02_formalizacion/14_dags_flujo_informacion.ipynb",    # Bloque II
        ROOT / "content/bloque_03_descubrimiento_ml/23_doble_desviacion.ipynb",      # Bloque III
        ROOT / "content/bloque_04_ia_causal/31_equidad_etica.ipynb"                  # Bloque IV
    ]
    failed = []
    for p in test_notebooks:
        if not p.exists():
            print(f"  ✗ missing {p}")
            failed.append(p)
            continue
        try:
            run_notebook(p)
        except Exception as e:
            print(f"  ✗ FAIL {p.name}: {e}")
            traceback.print_exc()
            failed.append(p)

    if failed:
        print(f"\n✗ Fallaron {len(failed)} notebooks")
        return 1
    print("\n✓ Smoke test superado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
