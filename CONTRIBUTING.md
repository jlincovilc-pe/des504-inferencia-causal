# Cómo contribuir / reportar errores

Este repositorio contiene **material del estudiante** del curso DES504. Las fuentes
tipográficas con las que se produjo el material no se distribuyen aquí, por lo que
las contribuciones se canalizan como **reportes de errores** y sugerencias.

## Reportar un error

Abre un *issue* usando la plantilla **Reporte de error en notebook** e incluye:

1. **Qué esperabas** que ocurriera y **qué ocurrió** realmente.
2. **Capítulo y celda** (por ejemplo: «Cap. 23, celda de DML, 2.ª de código»).
3. El **error completo** (traza de Python) si es un fallo de ejecución.
4. Tu **entorno**: sistema operativo, versión de Python y de las librerías clave
   (`python -c "import numpy, scipy, pandas; print(numpy.__version__, scipy.__version__, pandas.__version__)"`).
5. Si es un error **conceptual o matemático**, cita la sección del libro o la
   diapositiva correspondiente.

## Antes de reportar

```bash
python scripts/verificar_entorno.py             # comprueba entorno y datos
python recursos/ejemplo_paradoja_canonico.py    # resultado canónico del Cap. 1
```

Los notebooks son reproducibles con **semilla fija `42`**. Si un resultado numérico
difiere del documentado, revisa primero que la semilla y las versiones coincidan con
`requirements.txt`.

## Convenciones del material

- **Semilla canónica:** `42` en todo ejemplo numérico.
- **Cadena maestra GCE:** \(|\tau_{\mathrm{ATE}}| \le W_1 \le W^{G,1}\); \(W_1\) es
  **cota superior** de \(|\tau_{\mathrm{ATE}}|\).
- **Etiquetado de niveles:** Nivel 1 = localización; Nivel 2 = forma; Nivel 3 = geometría.
  Los capítulos 22–24 (meta-learners, DML, bosques causales) son **Nivel 1 + ML**.

## Licencia de las contribuciones

Al enviar una contribución aceptas que se distribuya bajo las licencias del
repositorio: CC BY-NC-SA 4.0 para contenidos y MIT para código.

© 2026 Universidad Nacional de Ingeniería (UNI), Perú.
