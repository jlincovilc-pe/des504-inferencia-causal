# Instalación en macOS

Guía para Mac con chip Apple Silicon (M1/M2/M3/M4) e Intel. Requiere Python 3.11.

## Opción A — Conda/Mamba (recomendada)

1. Instala Miniforge:

   ```bash
   brew install miniforge
   # o descarga el instalador desde https://github.com/conda-forge/miniforge/releases
   conda init zsh
   # cierra y reabre la terminal
   ```

   > **Apple Silicon:** usa la build `arm64` (es la que ofrece Homebrew por defecto
   > en Macs M-series). No mezcles builds `arm64` y `x86_64` en el mismo entorno.

2. Clona y crea el entorno:

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

Requiere Homebrew (https://brew.sh):

```bash
brew install python@3.11 graphviz
git clone https://github.com/jlincovilc-pe/des504-inferencia-causal.git
cd des504-inferencia-causal
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/registrar_kernel.py
python scripts/verificar_entorno.py
```

## Graphviz (para los DAGs del Bloque II)

```bash
brew install graphviz
```

## Verificación

```bash
python recursos/ejemplo_paradoja_canonico.py
```

Debe imprimir `ATE : -0.137 mmHg` y `W1 : 6.050 mmHg` (semilla 42).

## Notas para Apple Silicon

- Algunas ruedas (`torch`, `econml`) pueden requerir la versión `arm64`; con
  conda-forge suele resolverse automáticamente.
- Si aparece un error de `libomp`, instala `conda install -c conda-forge libomp`
  o `brew install libomp` según el caso.

## Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| `conda: command not found` | shell no recargado | `source ~/.zshrc` |
| El kernel `Python (DES504)` no aparece | kernel no registrado | `python scripts/registrar_kernel.py` |
| `dot` no encontrado | falta Graphviz | `brew install graphviz` |
| Entorno mixto roto | `x86_64` bajo Rosetta mezclado con `arm64` | recrea el entorno; usa el instalador `arm64` |

¿Dudas? Consulta [`docs/faq.md`](faq.md).
