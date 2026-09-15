# Inferencia Causal Aplicada con Python

Bienvenido al Jupyter Book de **Inferencia Causal Aplicada**: 32 capítulos desde los fundamentos de la causalidad hasta aplicaciones de inteligencia artificial causal.

## ¿Qué aprenderás?

### Bloque I: Fundamentación (Capítulos 1–12)
Métodos clásicos: RCT, matching, IPW, variables instrumentales, regression discontinuity, difference-in-differences, control sintético y mediación.

### Bloque II: Formalización (Capítulos 13–19)
Marco de Pearl: SCM, DAGs, backdoor, frontdoor, do-calculus y contrafactuales.

### Bloque III: Descubrimiento y ML Causal (Capítulos 20–27)
Descubrimiento causal, meta-learners, doble machine learning, efectos heterogéneos, paneles, off-policy evaluation y representaciones causales.

### Bloque IV: IA Causal (Capítulos 28–32)
RL causal, deep learning y LLMs, agentes semi-determinísticos, equidad y hoja de ruta.

## Cómo usar este libro

1. Lee secuencialmente los capítulos de cada bloque  
2. Ejecuta los notebooks (kernel **Python (lm_tools)**)  
3. Modifica los ejemplos y resuelve los ejercicios  

## Requisitos

- Python 3.10+ (recomendado: conda env `lm_tools`)  
- Estadística básica; pandas, numpy, matplotlib  

```bash
conda activate lm_tools
pip install -r requirements.txt && pip install -e .
python scripts/setup_local_data.py   # si aún no tienes data/
make lab
```

## Correcciones GCE v2.0 (2026-07-25)

Este Jupyter Book incorpora las **correcciones matemáticas de la jerarquía GCE** (Geometría de la Causalidad Estadística) aplicadas en julio 2026:

### Correcciones principales
- **Proposición de la Paradoja del Efecto Cero**: Cota corregida usando desigualdad de Jensen, independiente de σ
- **Ejemplo canónico**: Experimento de presión arterial con distribuciones N(105,8²) y N(135,10²) (media idéntica = 120 mmHg)
- **Cadena maestra**: Dirección correcta |τ_ATE| ≤ W₁ ≤ W^{G,1}
- **Axiomas 4a/4b**: Reformulación como estabilidad de funcionales (marginal e intervencional)
- **Validación numérica**: ATE ≈ -0.137, W₁ ≈ 6.050 mmHg verificados

### Nueva sección en Capítulo 1
El capítulo 1 ahora incluye la sección **"5bis. Experimento Canónico GCE: Presión Arterial"** con:
- Código ejecutable con parámetros de referencia
- Visualizaciones duales (distribuciones + jerarquía GCE)
- Assertions de validación matemática
- Interpretación clínica de medicina personalizada

Estas correcciones están descritas en el material teórico del curso.

## Licencia

CC-BY-NC-SA · Maestría en Ciencias e Ingeniería Estadística, UNI 2026

> **Datos:** la API `causal_book.data.load_dataset` está disponible (`pip install -e .`). Los notebooks del book resuelven rutas con `_resolve_data_dir()` / `content/datos` → `data/` para portabilidad local y Colab. Ambas vías son válidas.
