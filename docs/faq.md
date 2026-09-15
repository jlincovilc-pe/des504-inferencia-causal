# Preguntas frecuentes

## ¿Necesito saber programar para seguir el curso?

No para la parte conceptual: el libro y las diapositivas se leen solos. Para el
laboratorio necesitas Python básico; los notebooks están comentados paso a paso.

## ¿Qué instalo exactamente?

Un entorno con Python 3.11 y las librerías de `environment.yml` (o `requirements.txt`).
Sigue la guía de tu sistema: [Linux](instalacion-linux.md) · [macOS](instalacion-macos.md) ·
[Windows](instalacion-windows.md). Después:

```bash
python scripts/registrar_kernel.py
python scripts/verificar_entorno.py
```

## ¿Funciona en Windows?

Sí. No se usa `make`, no hay enlaces simbólicos y las rutas de datos son relativas.
Ver [instalación en Windows](instalacion-windows.md).

## ¿Necesito GPU?

No. Solo los capítulos 28–29 (opcionales) usan `torch`; el resto corre en CPU.

## ¿Por qué el ATE del Capítulo 1 es ≈ 0 si hay efecto?

Es la **Paradoja del Efecto Cero**: el tratamiento es una mezcla bimodal cuya media
coincide con la del control. El promedio no cambia, pero la distribución sí; eso lo
captura el Nivel 3 (`W₁ ≈ 6.050`). Reproducelo con:

```bash
python recursos/ejemplo_paradoja_canonico.py
```

## ¿Por qué `42` como semilla?

Es la **semilla canónica** del curso: garantiza que tus números coincidan con los del
libro, las diapositivas y el paper.

## Los números no me dan igual, ¿qué hago?

1. Confirma que no cambiaste la semilla.
2. Compara versiones de librerías con las de `requirements.txt`.
3. Ejecuta `python scripts/verificar_entorno.py`.
4. Si persiste, abre un *issue* con la plantilla de reporte ([CONTRIBUTING.md](../CONTRIBUTING.md)).

## ¿Puedo usar este material en mi propia clase?

Sí, bajo **CC BY-NC-SA 4.0**: puedes compartir y adaptar, con atribución, sin uso
comercial y compartiendo igual. Ver [`LICENSE`](../LICENSE).

## ¿Dónde están las fuentes del libro y las diapositivas?

No se distribuyen. Este repositorio contiene los **materiales** (PDF, notebooks,
datos), no las fuentes tipográficas con las que se produjeron.

## ¿Cómo cito el material?

Ver [`CITATION.cff`](../CITATION.cff) o la atribución sugerida en [`LICENSE`](../LICENSE).

## Un notebook consume mucha memoria, ¿cómo lo reduzco?

Los notebooks están dimensionados para equipos normales. Si tienes poca RAM, evita
*Run All* en los capítulos con simulaciones grandes y ejecútalos por secciones.

## ¿Puedo abrirlos en Google Colab?

Sí, subiendo el `.ipynb` y su carpeta `datos/` conservando la estructura relativa.
Ten en cuenta que algunas librerías (`lingam`, `econml`) deben instalarse en Colab
con `!pip install`.
