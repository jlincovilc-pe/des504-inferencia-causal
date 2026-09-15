#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Registra el kernel de Jupyter 'Python (DES504)' para este entorno.

Funciona igual en Linux, macOS y Windows. Ejecútalo con el entorno del curso
activado:

    conda activate des504
    python scripts/registrar_kernel.py
"""
from __future__ import annotations

import subprocess
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

KERNEL_NAME = "des504"
KERNEL_DISPLAY = "Python (DES504)"


def main() -> int:
    print(f"Intérprete: {sys.executable}")
    try:
        import ipykernel  # noqa: F401
    except ImportError:
        print("ERROR: 'ipykernel' no está instalado en este entorno.", file=sys.stderr)
        print("       Instálalo con: pip install ipykernel", file=sys.stderr)
        print("       O crea el entorno con: conda env create -f environment.yml", file=sys.stderr)
        return 1

    cmd = [
        sys.executable, "-m", "ipykernel", "install",
        "--user",
        "--name", KERNEL_NAME,
        "--display-name", KERNEL_DISPLAY,
    ]
    print("Ejecutando:", " ".join(cmd))
    resultado = subprocess.run(cmd)
    if resultado.returncode != 0:
        print("ERROR: no se pudo registrar el kernel.", file=sys.stderr)
        return resultado.returncode

    print(f"\n✓ Kernel '{KERNEL_DISPLAY}' registrado.")
    print("  Abre JupyterLab y selecciona ese kernel en los notebooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
