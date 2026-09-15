# Uso de los notebooks

## Dónde están

```text
notebooks/
├── Bloque_I/   → caps. 1–12   (Fundamentación)
├── Bloque_II/  → caps. 13–19  (Formalización / Pearl)
├── Bloque_III/ → caps. 20–27  (Descubrimiento causal y ML)
└── Bloque_IV/  → caps. 28–32  (IA causal)
```

Dentro de cada bloque:

- `notebooks/` — los archivos `.ipynb` del capítulo.
- `datos/` — los datasets que usa ese bloque (`datos/real/...` y `datos/synthetic/...`).

Los notebooks leen los datos con una ruta **relativa** (`../datos`), así que
funcionan sin configurar nada siempre que se abran desde su ubicación original.

## Abrirlos

```bash
conda activate des504
jupyter lab
```

Y navega hasta `notebooks/Bloque_I/notebooks/01_paradoja_efecto_cero_geometria_causalidad.ipynb`.

## Selección del kernel

Usa el kernel **Python (DES504)** (registrado por `scripts/registrar_kernel.py`).

Si no aparece en la lista:

1. Asegúrate de estar en el entorno correcto: `conda activate des504`.
2. Re-registra: `python scripts/registrar_kernel.py`.
3. Recarga la página de JupyterLab.

También puedes hacerlo a mano:

```bash
python -m ipykernel install --user --name des504 --display-name "Python (DES504)"
```

## Estructura típica de un notebook

Cada capítulo sigue el mismo patrón:

1. **Metadatos** — curso, capítulo, bloque, nivel GCE, dataset, versión.
2. **Marco teórico** — el concepto y su lugar en la jerarquía GCE.
3. **Código comentado** — implementación desde cero o con librerías.
4. **Interpretación** — lectura de los resultados (incluye contexto peruano/latinoamericano).
5. **Resumen y ejercicios** — cierre y práctica propuesta.

## Reproducibilidad

- **Semilla canónica:** `42` (`np.random.seed(42)` al inicio de cada notebook).
- No cambies la semilla si quieres comparar con los números del libro o del paper.
- Algunos notebooks usan archivos `truth_instructor_only.csv` con la verdad simulada;
  sirven para **medir el error** de los estimadores.

## Ejecutar todo

Desde JupyterLab puedes usar *Run → Run All Cells*. Para verificar el entorno
completo antes:

```bash
python scripts/verificar_entorno.py
```

## Capítulos que requieren dependencias opcionales

- **Caps. 28–29** (aprendizaje por refuerzo y arquitecturas deep): requieren
  `torch` → `pip install -r requirements-opcional.txt`.
- El resto del curso funciona con `requirements.txt`.

## Problemas frecuentes

| Síntoma | Solución |
|---------|----------|
| `FileNotFoundError: ../datos/...` | abre el notebook desde su carpeta original (no copies sueltos un `.ipynb`) |
| Kernel equivocado | selecciona **Python (DES504)** en el menú *Kernel* |
| `ModuleNotFoundError: econml / lingam` | activa el entorno `des504`; si persiste, `pip install -r requirements.txt` |
| Los gráficos no se muestran | *Run → Restart Kernel and Run All Cells* |

Ver también [`faq.md`](faq.md).
