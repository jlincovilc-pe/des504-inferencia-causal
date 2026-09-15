# Uso del Jupyter Book (versión web navegable)

`jupyter_book/` contiene la versión navegable del curso: los mismos 32 capítulos
como un libro web. Es la forma recomendada de **leer sin instalar nada** si ya está
publicado en línea.

## Leer en línea

Si el repositorio tiene GitHub Pages activado, el libro está disponible en:

```text
https://jlincovilc-pe.github.io/des504-inferencia-causal/
```

## Reconstruir el libro localmente

1. Activa el entorno:

   ```bash
   conda activate des504
   ```

2. Construye el HTML:

   ```bash
   cd jupyter_book
   jupyter-book build .
   ```

3. Sírvelo en el navegador:

   ```bash
   cd _build/html
   python -m http.server 8000
   ```

   Abre http://localhost:8000

> No se requiere `make`. Los comandos de arriba funcionan igual en Linux, macOS y
> Windows. En Linux/macOS puedes usar también `make build` dentro de `jupyter_book/`.

## Estructura

```text
jupyter_book/
├── intro.md          # portada
├── content/          # 32 capítulos (notebooks con nombres cortos)
├── data/             # datos reales y sintéticos
├── causal_book/      # utilidad load_dataset()
├── _config.yml       # configuración del book
└── _toc.yml          # tabla de contenidos
```

## Relación con `notebooks/`

- `notebooks/` es el **laboratorio**: notebooks ejecutables con nombres largos y
  datos por bloque. Es la fuente canónica para trabajar.
- `jupyter_book/content/` es la **versión de lectura**: los mismos capítulos con
  nombres cortos, ordenados como libro.

## Carga de datos programática

```python
from causal_book import load_dataset

df = load_dataset("nsw_mixtape")
student, truth = load_dataset("mediation_post_treatment", with_truth=True)
```

La variable de entorno `CAUSAL_BOOK_DATA` permite apuntar a otra ubicación de datos
si es necesario.

## Problemas frecuentes

| Síntoma | Solución |
|---------|----------|
| `jupyter-book: command not found` | `pip install -r requirements.txt` (incluye `jupyter-book`) |
| La build no encuentra `content/` | ejecuta el comando desde `jupyter_book/` |
| Datos no encontrados | verifica que exista `jupyter_book/data/`; o define `CAUSAL_BOOK_DATA` |
