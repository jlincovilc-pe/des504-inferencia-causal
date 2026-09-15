# DES504 · Inferencia Causal Aplicada con Python

**Curso:** DES504 · Maestría en Ciencias e Ingeniería Estadística
**Institución:** Universidad Nacional de Ingeniería (UNI) · Lima, Perú
**Profesor:** Dr. Jaime Lincovil
**Año:** 2026
**Marco unificador:** Geometría de la Causalidad Estadística (**GCE**)
**Semilla canónica de reproducibilidad:** `42`

Repositorio de **material del estudiante**: libro de lectura, diapositivas de aula, 32 notebooks de laboratorio con sus datos y una versión web navegable (Jupyter Book).

---

## Contenido del repositorio

| Carpeta | Qué es | Cómo se usa |
|---------|--------|-------------|
| `libro/` | Monografía completa en PDF (32 capítulos) | Leer antes de cada sesión |
| `diapositivas/` | 32 presentaciones en PDF (aula, 16:9) | Seguir la clase |
| `notebooks/` | 32 notebooks ejecutables + datasets por bloque | Laboratorio |
| `jupyter_book/` | Fuente del libro web (versión navegable) | Leer en línea / reconstruir |
| `paper/` | *Geometría de la Causalidad Estadística* (paper, ~13 pp.) | Lectura avanzada opcional |
| `recursos/` | Script reproducible del experimento canónico del Cap. 1 | Reproducir el resultado insignia |

> **Nota:** este repositorio distribuye los **materiales** (PDF, notebooks, datos), no las fuentes tipográficas con las que fueron producidos.

---

## Instalación rápida (3 pasos)

Elige tu sistema operativo. Se recomienda **conda/mamba** por simplicidad multiplataforma.

```bash
git clone https://github.com/<usuario>/des504-inferencia-causal.git
cd des504-inferencia-causal
conda env create -f environment.yml
conda activate des504
python scripts/registrar_kernel.py        # registra el kernel "Python (DES504)"
python scripts/verificar_entorno.py       # comprueba dependencias y datos
jupyter lab
```

Guías detalladas y alternativas con `pip`/`venv`:

- [Instalación en Linux](docs/instalacion-linux.md)
- [Instalación en macOS](docs/instalacion-macos.md)
- [Instalación en Windows](docs/instalacion-windows.md)
- [Uso de los notebooks](docs/uso-notebooks.md)
- [Uso del Jupyter Book](docs/uso-jupyter-book.md)
- [Preguntas frecuentes](docs/faq.md)

### Verificación rápida

```bash
python recursos/ejemplo_paradoja_canonico.py
```

Salida esperada (semilla 42):

```
Nivel 1 ATE      : -0.137 mmHg
Nivel 2 D_KL     : 0.364 nats
Nivel 3 W1       : 6.050 mmHg
Cota dual        : 6.029 <= W1 = 6.050  [OK]
Cadena maestra   : |ATE| = 0.137 <= W1 = 6.050  [OK]
```

---

## El marco del curso: la cadena maestra

Bajo SUTVA, toda pregunta causal se formula como un funcional de discrepancia no negativo entre las leyes contrafactuales \(\mathbb{P}_{Y(1)}\) y \(\mathbb{P}_{Y(0)}\). La columna vertebral del curso es:

$$|\tau_{\mathrm{ATE}}| \;\le\; W_1(\mathbb{P}_{Y(1)},\mathbb{P}_{Y(0)}) \;\le\; W^{G,1}$$

- **Nivel 1 · Localización:** ¿cambió el centro? → \(|\tau_{\mathrm{ATE}}|\)
- **Nivel 2 · Forma:** ¿cambió la distribución? → divergencias \(f\) (KL, TV)
- **Nivel 3 · Geometría:** ¿cuál es el costo del cambio? → \(W_1\) y su refinamiento causal \(W^{G,1}\)

Consecuencia clave: \(W_1\) es una **cota superior** del efecto medio. Un \(W_1\) grande **no** implica un ATE grande; esa falsedad es la **Paradoja del Efecto Cero** (ATE ≈ 0 con \(W_1 \gg 0\)), el experimento del Capítulo 1.

---

## Mapa de capítulos

Ver **`docs/`** para instrucciones. Cada capítulo tiene su diapositiva y su notebook.

### Bloque I — Fundamentación (caps. 1–12)

| # | Título | Diapositivas | Notebook |
|--:|--------|--------------|----------|
| 01 | Paradoja del Efecto Cero | [PDF](diapositivas/capitulo01.pdf) | [01_paradoja_efecto_cero_geometria_causalidad.ipynb](notebooks/Bloque_I/notebooks/01_paradoja_efecto_cero_geometria_causalidad.ipynb) |
| 02 | Problema fundamental y aleatorización | [PDF](diapositivas/capitulo02.pdf) | [02_problema_fundamental_relevancia_aleatorizacion.ipynb](notebooks/Bloque_I/notebooks/02_problema_fundamental_relevancia_aleatorizacion.ipynb) |
| 03 | El arte del matching | [PDF](diapositivas/capitulo03.pdf) | [03_arte_matching_dimensiones_distancias.ipynb](notebooks/Bloque_I/notebooks/03_arte_matching_dimensiones_distancias.ipynb) |
| 04 | IPW y doble robustez | [PDF](diapositivas/capitulo04.pdf) | [04_ipw_santo_grial_doble_robustez.ipynb](notebooks/Bloque_I/notebooks/04_ipw_santo_grial_doble_robustez.ipynb) |
| 05 | Variables instrumentales | [PDF](diapositivas/capitulo05.pdf) | [05_abismo_lo_no_observable_rescate.ipynb](notebooks/Bloque_I/notebooks/05_abismo_lo_no_observable_rescate.ipynb) |
| 06 | LATE y taxonomía de respondientes | [PDF](diapositivas/capitulo06.pdf) | [06_late_taxonomia_respondientes.ipynb](notebooks/Bloque_I/notebooks/06_late_taxonomia_respondientes.ipynb) |
| 07 | Regresión discontinua (RDD) | [PDF](diapositivas/capitulo07.pdf) | [07_regression_discontinuity_design_geometria_umbral.ipynb](notebooks/Bloque_I/notebooks/07_regression_discontinuity_design_geometria_umbral.ipynb) |
| 08 | Diferencias en diferencias (DiD) | [PDF](diapositivas/capitulo08.pdf) | [08_difference_in_differences_arquitectura_tiempo.ipynb](notebooks/Bloque_I/notebooks/08_difference_in_differences_arquitectura_tiempo.ipynb) |
| 09 | Control sintético | [PDF](diapositivas/capitulo09.pdf) | [09_control_sintetico_ingenieria_contrafactual.ipynb](notebooks/Bloque_I/notebooks/09_control_sintetico_ingenieria_contrafactual.ipynb) |
| 10 | Mediación causal | [PDF](diapositivas/capitulo10.pdf) | [10_mediacion_causal_descomposicion_efectos_mecanismos.ipynb](notebooks/Bloque_I/notebooks/10_mediacion_causal_descomposicion_efectos_mecanismos.ipynb) |
| 11 | Robustez y validación | [PDF](diapositivas/capitulo11.pdf) | [11_robustez_validacion_contextos_especiales.ipynb](notebooks/Bloque_I/notebooks/11_robustez_validacion_contextos_especiales.ipynb) |
| 12 | Guía de selección de métodos | [PDF](diapositivas/capitulo12.pdf) | [12_guia_practica_seleccion_metodos_sintesis.ipynb](notebooks/Bloque_I/notebooks/12_guia_practica_seleccion_metodos_sintesis.ipynb) |

### Bloque II — Formalización / Pearl (caps. 13–19)

| # | Título | Diapositivas | Notebook |
|--:|--------|--------------|----------|
| 13 | Modelos causales estructurales (SCM) | [PDF](diapositivas/capitulo13.pdf) | [13_modelos_causales_estructurales_scm_anatomia_mecanismo.ipynb](notebooks/Bloque_II/notebooks/13_modelos_causales_estructurales_scm_anatomia_mecanismo.ipynb) |
| 14 | DAGs y flujo de información | [PDF](diapositivas/capitulo14.pdf) | [14_dags_estructuras_fundamentales_flujo_informacion.ipynb](notebooks/Bloque_II/notebooks/14_dags_estructuras_fundamentales_flujo_informacion.ipynb) |
| 15 | Criterio backdoor | [PDF](diapositivas/capitulo15.pdf) | [15_criterio_backdoor_arte_ajuste.ipynb](notebooks/Bloque_II/notebooks/15_criterio_backdoor_arte_ajuste.ipynb) |
| 16 | Criterio frontdoor | [PDF](diapositivas/capitulo16.pdf) | [16_criterio_frontdoor_identificacion_sin_observar_confusores.ipynb](notebooks/Bloque_II/notebooks/16_criterio_frontdoor_identificacion_sin_observar_confusores.ipynb) |
| 17 | Naturaleza de las causas | [PDF](diapositivas/capitulo17.pdf) | [17_naturaleza_causas_singular_general_empirico.ipynb](notebooks/Bloque_II/notebooks/17_naturaleza_causas_singular_general_empirico.ipynb) |
| 18 | Do-cálculo | [PDF](diapositivas/capitulo18.pdf) | [18_do_calculus_sistema_axiomatico_causalidad.ipynb](notebooks/Bloque_II/notebooks/18_do_calculus_sistema_axiomatico_causalidad.ipynb) |
| 19 | Contrafactuales | [PDF](diapositivas/capitulo19.pdf) | [19_contrafactuales_tercer_nivel_escalera.ipynb](notebooks/Bloque_II/notebooks/19_contrafactuales_tercer_nivel_escalera.ipynb) |

### Bloque III — Descubrimiento causal y ML (caps. 20–27)

| # | Título | Diapositivas | Notebook |
|--:|--------|--------------|----------|
| 20 | Descubrimiento causal | [PDF](diapositivas/capitulo20.pdf) | [20_descubrimiento_causal_flujo_trabajo_restricciones.ipynb](notebooks/Bloque_III/notebooks/20_descubrimiento_causal_flujo_trabajo_restricciones.ipynb) |
| 21 | Aprendizaje causal y jerarquía de Pearl | [PDF](diapositivas/capitulo21.pdf) | [21_fundamentos_aprendizaje_causal_jerarquia_pearl.ipynb](notebooks/Bloque_III/notebooks/21_fundamentos_aprendizaje_causal_jerarquia_pearl.ipynb) |
| 22 | Meta-learners | [PDF](diapositivas/capitulo22.pdf) | [22_meta_learners_inferencia_causal_stx.ipynb](notebooks/Bloque_III/notebooks/22_meta_learners_inferencia_causal_stx.ipynb) |
| 23 | Doble machine learning (DML) | [PDF](diapositivas/capitulo23.pdf) | [23_doble_desviacion_aprendizaje_automatico_ortogonal.ipynb](notebooks/Bloque_III/notebooks/23_doble_desviacion_aprendizaje_automatico_ortogonal.ipynb) |
| 24 | Efectos heterogéneos y bosques causales | [PDF](diapositivas/capitulo24.pdf) | [24_efectos_heterogeneos_arboles_causales_bosques.ipynb](notebooks/Bloque_III/notebooks/24_efectos_heterogeneos_arboles_causales_bosques.ipynb) |
| 25 | Series de tiempo y paneles + ML | [PDF](diapositivas/capitulo25.pdf) | [25_causalidad_series_tiempo_paneles_machine.ipynb](notebooks/Bloque_III/notebooks/25_causalidad_series_tiempo_paneles_machine.ipynb) |
| 26 | Off-policy evaluation y bandits | [PDF](diapositivas/capitulo26.pdf) | [26_off_policy_evaluation_bandits_politica.ipynb](notebooks/Bloque_III/notebooks/26_off_policy_evaluation_bandits_politica.ipynb) |
| 27 | Representaciones causales | [PDF](diapositivas/capitulo27.pdf) | [27_aprendizaje_representaciones_causales_modelos_generativos.ipynb](notebooks/Bloque_III/notebooks/27_aprendizaje_representaciones_causales_modelos_generativos.ipynb) |

### Bloque IV — IA causal (caps. 28–32)

| # | Título | Diapositivas | Notebook |
|--:|--------|--------------|----------|
| 28 | Aprendizaje por refuerzo causal | [PDF](diapositivas/capitulo28.pdf) | [28_aprendizaje_refuerzo_causal_control_secuencial.ipynb](notebooks/Bloque_IV/notebooks/28_aprendizaje_refuerzo_causal_control_secuencial.ipynb) |
| 29 | Arquitecturas de IA causal | [PDF](diapositivas/capitulo29.pdf) | [29_arquitecturas_ia_causal_integracion_deep.ipynb](notebooks/Bloque_IV/notebooks/29_arquitecturas_ia_causal_integracion_deep.ipynb) |
| 30 | Agentes causales semi-determinísticos | [PDF](diapositivas/capitulo30.pdf) | [30_agentes_estadisticos_causal_semi_deterministicos.ipynb](notebooks/Bloque_IV/notebooks/30_agentes_estadisticos_causal_semi_deterministicos.ipynb) |
| 31 | Equidad y ética | [PDF](diapositivas/capitulo31.pdf) | [31_equidad_etica_regulacion_desde_perspectiva.ipynb](notebooks/Bloque_IV/notebooks/31_equidad_etica_regulacion_desde_perspectiva.ipynb) |
| 32 | Hoja de ruta de la IA causal | [PDF](diapositivas/capitulo32.pdf) | [32_hoja_ruta_ia_causal_problemas.ipynb](notebooks/Bloque_IV/notebooks/32_hoja_ruta_ia_causal_problemas.ipynb) |

---

## Principios del curso

1. **La causalidad requiere supuestos.** No hay almuerzo gratis: todo método descansa en supuestos no testeables (CIA, exclusión, tendencias paralelas).
2. **Validar siempre.** Placebos, robustez y análisis de sensibilidad son obligatorios.
3. **Múltiples métodos > uno.** Si IPW, DML y bosques causales coinciden, la confianza sube; si divergen, hay algo que investigar.
4. **Transparencia > elegancia.** Reportar supuestos, puntos de fallo y limitaciones.
5. **Proofs-to-Python.** Toda cota demostrada se verifica con `assert` en código; todo número reportado es reproducible con semilla fija (`42`).

---

## Requisitos

- Python 3.11 (recomendado)
- ~2 GB de espacio para el entorno; ~500 MB para los datos ya incluidos
- No se requiere GPU (los capítulos 28–29 de *deep learning* son opcionales)

Ver [`docs/`](docs/) para la instalación detallada en cada sistema operativo.

---

## Licencia y citación

- **Contenidos** (libro, diapositivas, notebooks, datos): CC BY-NC-SA 4.0 → [`LICENSE`](LICENSE)
- **Código** (scripts): MIT → [`LICENSE-CODE`](LICENSE-CODE)
- Cómo citar: [`CITATION.cff`](CITATION.cff)

Las fuentes tipográficas (Typst/LaTeX) del material **no** se distribuyen en este repositorio.

© 2026 Universidad Nacional de Ingeniería (UNI), Perú. Uso educativo / académico · DES504.
