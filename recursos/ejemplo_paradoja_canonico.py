"""
Ejemplo canónico de la Paradoja del Efecto Cero
Versión de referencia para el libro y notebooks GCE v2
Material de referencia del curso DES504.
"""

import numpy as np
from scipy.stats import wasserstein_distance
from scipy.special import rel_entr

np.random.seed(42)
n = 5000

# Presion arterial: Control unimodal; Tratamiento bimodal con LA MISMA MEDIA
# Media de la mezcla: (105 + 135)/2 = 120 = media del control
Y0 = np.random.normal(120, 12, n)
Y1 = np.concatenate([np.random.normal(105,  8, n//2),   # respondedores
                     np.random.normal(135, 10, n//2)])  # no respondedores

# --- Jerarquia GCE ---
tau_ate = np.mean(Y1) - np.mean(Y0)

bins = np.linspace(60, 180, 61)
p0, _ = np.histogram(Y0, bins=bins, density=True)
p1, _ = np.histogram(Y1, bins=bins, density=True)
kl_div = np.sum(rel_entr(p1 + 1e-10, p0 + 1e-10)) * (bins[1] - bins[0])

w1 = wasserstein_distance(Y0, Y1)

cota_dual = np.mean(np.abs(Y1 - 120)) - np.mean(np.abs(Y0 - 120))

print(f"Nivel 1 ATE      : {tau_ate:.3f} mmHg  <- ciego a la reconfiguracion")
print(f"Nivel 2 D_KL     : {kl_div:.3f} nats   <- detecta cambio de forma")
print(f"Nivel 3 W1       : {w1:.3f} mmHg  <- costo de transporte")
print(f"Cota dual        : {cota_dual:.3f} <= W1 = {w1:.3f}  [OK]")
print(f"Cadena maestra   : |ATE| = {abs(tau_ate):.3f} <= W1 = {w1:.3f}  [OK]")
assert abs(tau_ate) <= w1 + 1e-6, "Violacion |ATE| <= W1"
assert cota_dual   <= w1 + 1e-6, "Violacion dualidad K-R"
