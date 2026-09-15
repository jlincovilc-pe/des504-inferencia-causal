# Notebooks de laboratorio

32 notebooks ejecutables, uno por capítulo, agrupados en cuatro bloques. Cada
bloque es autocontenido: incluye sus propios datos en `datos/`.

## Bloques

| Bloque | Capítulos | Tema | Nivel GCE predominante |
|--------|-----------|------|------------------------|
| **I** | 1–12 | Fundamentación: RCT, matching, IPW, IV, LATE, RDD, DiD, control sintético, mediación, robustez, selección | Nivel 1 (localización) |
| **II** | 13–19 | Formalización: SCM, DAGs, backdoor, frontdoor, do-cálculo, contrafactuales | Identificación / forma |
| **III** | 20–27 | Descubrimiento causal y ML: PC, meta-learners, DML, bosques causales, series y paneles, OPE, representaciones | Precondición y Nivel 1 + ML |
| **IV** | 28–32 | IA causal: RL causal, arquitecturas deep, agentes, equidad, hoja de ruta | Aplicaciones de N1–N3 |

> **Nota de etiquetado GCE.** Los capítulos 22–24 (meta-learners, DML, bosques
> causales) son **Nivel 1 con ML**, no “Nivel 3”. El Nivel 3 (geometría, \(W_1\),
> transporte óptimo) corresponde a los métodos de costo de reasignación.

## Estructura

```text
notebooks/
├── Bloque_I/
│   ├── notebooks/    # 12 archivos .ipynb
│   └── datos/        # real/ y synthetic/
├── Bloque_II/  ·  Bloque_III/  ·  Bloque_IV/
└── README.md
```

## Cómo ejecutarlos

```bash
conda activate des504
jupyter lab
```

Abre un notebook y selecciona el kernel **Python (DES504)**. Los datos se resuelven
con la ruta relativa `../datos`, así que abre cada notebook desde su carpeta original.

## Datasets

- **Reales:** `nsw_mixtape`, `nhefs`, `close_college`, `thornton_hiv`, `texas`, `mortgages`.
- **Sintéticos:** `rct`, `matching`, `iv`, `rdd`, `did`, `mediation`, `panel`
  (cada uno con su carpeta y, cuando corresponde, `truth_instructor_only.csv` con la
  verdad simulada para medir el error).

## Reproducibilidad

Semilla canónica `42`. No la cambies si quieres comparar con los números del libro
y del paper.

## Detalles

Consulta [`../docs/uso-notebooks.md`](../docs/uso-notebooks.md).
