"""
Genera 6 gráficos de precios para el laboratorio "¿GBM o Merton?".
- 3 trayectorias GBM
- 3 trayectorias Merton
Los parámetros no aparecen en la figura.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE, "assets", "laboratorio_graficos")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def simular(tipo, seed, S0=100.0, mu=0.05, sigma=0.2, T=1.0, steps=252):
    np.random.seed(seed)
    dt = T / steps
    prices = np.zeros(steps + 1)
    prices[0] = S0
    for t in range(1, steps + 1):
        Z = np.random.normal(0, 1)
        if tipo == "GBM":
            prices[t] = prices[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
        else:
            lam, mu_J, sigma_J = 1.5, -0.10, 0.15
            N = np.random.poisson(lam * dt)
            J = np.random.lognormal(mu_J, sigma_J) if N > 0 else 1
            prices[t] = prices[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z) * (J ** N)
    return prices

def guardar_grafico(prices, nombre, titulo):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(prices, lw=1.5)
    ax.set_title(titulo, fontsize=14)
    ax.set_xlabel("Días")
    ax.set_ylabel("Precio")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, nombre), dpi=150, bbox_inches="tight")
    plt.close()

# Configuración: 3 GBM y 3 Merton
config = [
    ("GBM", 1),
    ("Merton", 2),
    ("GBM", 3),
    ("Merton", 4),
    ("GBM", 5),
    ("Merton", 6),
]

for tipo, seed in config:
    prices = simular(tipo, seed)
    guardar_grafico(
        prices,
        f"grafico_{seed}.png",
        f"Gráfico {seed}"
    )

print(f"6 gráficos guardados en {OUTPUT_DIR}")
