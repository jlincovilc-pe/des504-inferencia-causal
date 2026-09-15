# Instalación en Windows

Guía para Windows 10/11. Compatible con **PowerShell**, **cmd** y **Git Bash**.
Requiere Python 3.11.

> **Importante:** este repositorio **no necesita `make`**. Todos los comandos de
> instalación y verificación funcionan igual en PowerShell, cmd y Git Bash.

## Opción A — Conda/Mamba (recomendada)

1. Instala Miniforge for Windows desde
   https://github.com/conda-forge/miniforge/releases (archivo `...-Windows-x86_64.exe`).

   Durante la instalación, deja marcada la opción para registrar Miniforge en el PATH
   (o usa el **Miniforge Prompt** que se crea en el menú Inicio).

2. Clona el repositorio. Si no tienes Git, instálalo desde https://git-scm.com/download/win

   ```powershell
   git clone https://github.com/jlincovilc-pe/des504-inferencia-causal.git
   cd des504-inferencia-causal
   ```

3. Crea el entorno y actívalo:

   ```powershell
   conda env create -f environment.yml
   conda activate des504
   ```

4. Registra el kernel y verifica:

   ```powershell
   python scripts\registrar_kernel.py
   python scripts\verificar_entorno.py
   ```

5. Abre JupyterLab:

   ```powershell
   jupyter lab
   ```

## Opción B — venv + pip (PowerShell)

```powershell
git clone https://github.com/jlincovilc-pe/des504-inferencia-causal.git
cd des504-inferencia-causal
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts\registrar_kernel.py
python scripts\verificar_entorno.py
```

> Si PowerShell bloquea la activación del entorno con un error de *execution policy*,
> ejecuta una vez: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
> (o usa `cmd` con `.venv\Scripts\activate.bat`).

## Graphviz (para los DAGs del Bloque II)

Descarga e instala el instalador oficial: https://graphviz.org/download/
Marca la opción **"Add Graphviz to the system PATH"**. Después reinicia la terminal.

## Rutas y datos

- Los notebooks usan rutas **relativas**; no hay rutas absolutas que ajustar.
- No se usan enlaces simbólicos, por lo que el repositorio funciona sin permisos
  especiales de desarrollador.

## Verificación

```powershell
python recursos\ejemplo_paradoja_canonico.py
```

Debe imprimir `ATE : -0.137 mmHg` y `W1 : 6.050 mmHg` (semilla 42).

## Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| `conda` no reconocido | No se marcó "Add to PATH" | usa el **Miniforge Prompt** |
| `.venv\Scripts\Activate.ps1` bloqueado | política de ejecución | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| El kernel `Python (DES504)` no aparece | kernel no registrado | `python scripts\registrar_kernel.py` |
| `dot` no reconocido | Graphviz sin PATH | reinstala marcando la casilla de PATH |
| Acentos raros en la consola | codificación de la terminal | usa JupyterLab (no la consola) para las salidas |

¿Dudas? Consulta [`docs/faq.md`](faq.md).
