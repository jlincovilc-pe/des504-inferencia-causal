#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica que el entorno y los datos del curso DES504 estén listos.

Comprueba:
  1. Versión de Python.
  2. Dependencias del núcleo (obligatorias) y opcionales.
  3. Presencia de los datos del pack y del Jupyter Book.
  4. El experimento canónico del Cap. 1 (semilla 42) y sus dos desigualdades.

Uso:
    python scripts/verificar_entorno.py

Devuelve código de salida 0 si todo está correcto, 1 en caso contrario.
Funciona igual en Linux, macOS y Windows.
"""
from __future__ import annotations

import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent

OBLIGATORIAS = [
    ("numpy", "numpy"),
    ("pandas", "pandas"),
    ("scipy", "scipy"),
    ("matplotlib", "matplotlib"),
    ("seaborn", "seaborn"),
    ("statsmodels", "statsmodels"),
    ("sklearn", "scikit-learn"),
    ("networkx", "networkx"),
]

OPCIONALES = [
    ("ot", "POT"),
    ("causal_learn", "causal-learn"),
    ("lingam", "lingam"),
    ("doubleml", "DoubleML"),
    ("econml", "econml"),
    ("linearmodels", "linearmodels"),
    ("torch", "torch"),
]

ok = True


def fallo(msg: str) -> None:
    global ok
    ok = False
    print(f"  ✗ {msg}")


def bien(msg: str) -> None:
    print(f"  ✓ {msg}")


def verificar_python() -> None:
    print("\n[1/4] Versión de Python")
    v = sys.version_info
    if v >= (3, 10):
        bien(f"Python {v.major}.{v.minor}.{v.micro}")
    else:
        fallo(f"Python {v.major}.{v.minor} — se requiere 3.10 o superior")


def verificar_dependencias() -> None:
    print("\n[2/4] Dependencias")
    for modulo, paquete in OBLIGATORIAS:
        try:
            m = __import__(modulo)
            version = getattr(m, "__version__", "?")
            bien(f"{paquete} {version}")
        except ImportError:
            fallo(f"{paquete} no instalado (obligatorio) — pip install -r requirements.txt")
    for modulo, paquete in OPCIONALES:
        try:
            m = __import__(modulo)
            version = getattr(m, "__version__", "?")
            bien(f"{paquete} {version} (opcional)")
        except ImportError:
            print(f"  – {paquete} no instalado (opcional; se usa en capítulos avanzados)")


def verificar_datos() -> None:
    print("\n[3/4] Datos")
    bloques = [RAIZ / "notebooks" / f"Bloque_{b}" / "datos"
               for b in ("I", "II", "III", "IV")]
    for d in bloques:
        if d.is_dir() and any(d.rglob("*.csv")):
            n = len(list(d.rglob("*.csv")))
            bien(f"{d.relative_to(RAIZ)} ({n} CSV)")
        else:
            fallo(f"faltan datos en {d.relative_to(RAIZ)}")
    jb = RAIZ / "jupyter_book" / "data"
    if jb.is_dir():
        bien(f"{jb.relative_to(RAIZ)}")
    else:
        fallo("falta jupyter_book/data")


def verificar_experimento_canonico() -> None:
    print("\n[4/4] Experimento canónico del Cap. 1 (semilla 42)")
    try:
        import numpy as np
        from scipy.stats import wasserstein_distance
    except ImportError:
        fallo("numpy/scipy no disponibles; se omite la verificación numérica")
        return

    np.random.seed(42)
    n = 5000
    y0 = np.random.normal(120, 12, n)
    y1 = np.concatenate([np.random.normal(105, 8, n // 2),
                         np.random.normal(135, 10, n // 2)])
    tau = float(np.mean(y1) - np.mean(y0))
    w1 = float(wasserstein_distance(y0, y1))
    cota_dual = float(np.mean(np.abs(y1 - 120)) - np.mean(np.abs(y0 - 120)))

    print(f"    ATE = {tau:.3f} mmHg · W1 = {w1:.3f} mmHg · cota dual = {cota_dual:.3f}")
    try:
        assert abs(tau) <= w1 + 1e-6, "violación |ATE| <= W1"
        assert cota_dual <= w1 + 1e-6, "violación dualidad K-R"
        bien(f"cadena maestra: |ATE| = {abs(tau):.3f} <= W1 = {w1:.3f}")
        bien(f"dualidad K-R : cota dual = {cota_dual:.3f} <= W1 = {w1:.3f}")
        if abs(tau + 0.137) < 0.03 and abs(w1 - 6.050) < 0.15:
            bien("valores coinciden con los documentados (ATE ≈ -0.137, W1 ≈ 6.050)")
        else:
            print("  – los valores difieren de los documentados; revisa versiones de numpy/scipy")
    except AssertionError as exc:
        fallo(str(exc))


def main() -> int:
    print("=" * 62)
    print(" Verificación del entorno · DES504 · Inferencia Causal Aplicada")
    print("=" * 62)
    verificar_python()
    verificar_dependencias()
    verificar_datos()
    verificar_experimento_canonico()
    print("\n" + "=" * 62)
    if ok:
        print(" RESULTADO: entorno listo. Abre JupyterLab:  jupyter lab")
    else:
        print(" RESULTADO: hay problemas. Revisa los ✗ de arriba.")
        print(" Guías: docs/instalacion-*.md  ·  docs/faq.md")
    print("=" * 62)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
