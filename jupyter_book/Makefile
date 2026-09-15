# Jupyter Book — comandos de conveniencia (Linux/macOS)
#
# En Windows no necesitas make: usa directamente los comandos equivalentes
# documentados en ../docs/uso-jupyter-book.md
#
#   jupyter-book build .
#   cd _build/html ; python -m http.server 8000
#
# Uso:
#   make build   — genera el HTML del libro en _build/html
#   make serve   — sirve el HTML en http://localhost:8000
#   make clean   — borra _build y cachés

PYTHON ?= python
.PHONY: help build serve clean

help:
	@echo "Objetivos: build | serve | clean"
	@echo "Python usado: $(PYTHON)"

build:
	jupyter-book build .

serve:
	cd _build/html && $(PYTHON) -m http.server 8000

clean:
	rm -rf _build
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
	find . -name '.ipynb_checkpoints' -type d -prune -exec rm -rf {} +

.DEFAULT_GOAL := help
