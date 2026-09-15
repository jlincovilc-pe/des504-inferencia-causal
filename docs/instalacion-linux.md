# Instalación en Linux

Guía probada en distribuciones basadas en Debian/Ubuntu y en Fedora. Requiere
Python 3.11.

## Opción A — Conda/Mamba (recomendada)

1. Instala Miniforge (incluye `mamba`, más rápido que `conda`):

   ```bash
   curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
   bash Miniforge3-Linux-x86_64.sh
   # cierra y reabre la terminal
   ```

   > En procesadores ARM (por ejemplo Raspberry Pi o servidores Ampere) usa
   > `Miniforge3-Linux-aarch64.sh`.

2. Clona el repositorio y crea el entorno:

   ```bash
   git clone https://github.com/jlincovilc-pe/des504-inferencia-causal.git
   cd des504-inferencia-causal
   conda env create -f environment.yml
   conda activate des504
   ```

3. Registra el kernel y verifica:

   ```bash
   python scripts/registrar_kernel.py
   python scripts/verificar_entorno.py
   ```

4. Abre JupyterLab:

   ```bash
   jupyter lab
   ```

## Opción B — venv + pip

```bash
sudo apt update && sudo apt install -y python3.11 python3.11-venv graphviz
git clone https://github.com/jlincovilc-pe/des504-inferencia-causal.git
cd des504-inferencia-causal
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/registrar_kernel.py
python scripts/verificar_entorno.py
```

## Dependencia del sistema: Graphviz

Algunos notebooks del Bloque II dibujan DAGs con `networkx` + `pydot`, que necesitan
el binario **Graphviz**:

- Debian/Ubuntu: `sudo apt install graphviz`
- Fedora: `sudo dnf install graphviz`
- Arch: `sudo pacman -S graphviz`

Si no lo instalas, los notebooks funcionan salvo las celdas que exportan grafos a
imagen.

## Verificación

```bash
python recursos/ejemplo_paradoja_canonico.py
```

Debe imprimir `ATE : -0.137 mmHg` y `W1 : 6.050 mmHg` (semilla 42).

## Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| `conda: command not found` | shell no recargado | cierra y reabre la terminal, o `source ~/.bashrc` |
| El kernel `Python (DES504)` no aparece en Jupyter | kernel no registrado para este usuario | `python scripts/registrar_kernel.py` |
| `ExecutableNotFound: dot` | falta Graphviz | instala Graphviz (arriba) |
| Error al compilar `torch` | falta de espacio/tiempo | usa `requirements-opcional.txt` solo si harás los caps. 28–29 |

¿Dudas? Consulta [`docs/faq.md`](faq.md).
