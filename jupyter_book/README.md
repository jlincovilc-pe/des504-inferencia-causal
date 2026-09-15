# Jupyter Book

Versión navegable del curso: los 32 capítulos como libro web. Es la forma
recomendada de leer el material sin instalar nada (si está publicado en línea).

## Leer en línea

```text
https://<usuario>.github.io/des504-inferencia-causal/
```

## Construir localmente

```bash
conda activate des504
cd jupyter_book
jupyter-book build .
cd _build/html
python -m http.server 8000     # abre http://localhost:8000
```

No se requiere `make`. También hay un `Makefile` para quien lo prefiera en Linux/macOS:

```bash
make build
make serve
```

## Contenido

- `intro.md` — portada del libro.
- `content/` — los 32 capítulos (notebooks, nombres cortos).
- `data/` — datos reales y sintéticos.
- `causal_book/` — utilidad `load_dataset()` para cargar datos por nombre lógico.

## Relación con `notebooks/`

`notebooks/` es el laboratorio (notebooks ejecutables con nombres largos y datos por
bloque); `jupyter_book/content/` es la versión de lectura, con los mismos capítulos
ordenados como libro.

Detalles de uso en [`../docs/uso-jupyter-book.md`](../docs/uso-jupyter-book.md).
