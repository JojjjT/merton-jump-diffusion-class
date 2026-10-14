"""
Precalcula una malla de trayectorias Merton para el demo publicable.
Salida: data/trayectorias.json consumido por demo_trayectorias.qmd.

El sitio publicado no tiene kernel Python, así que la interactividad
usa trayectorias precalculadas + plotly.js (funciona 100% sin servidor).
"""
import json
import os
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE, "data")
os.makedirs(OUT_DIR, exist_ok=True)

S0, MU, T, STEPS = 100.0, 0.05, 1.0, 120
DT = T / STEPS

LAMBDAS = [0, 1, 2, 3, 4, 5]
MU_JS = [-0.15, -0.08, 0.0, 0.08, 0.15]
SIGMA_JS = [0.05, 0.12, 0.25]
SIGMAS = [0.15, 0.2, 0.3]
SEEDS = [7]


def simular(lam, mu_J, sigma_J, sigma, seed):
    np.random.seed(seed)
    prices = np.zeros(STEPS + 1)
    prices[0] = S0
    saltos = 0
    k = np.exp(mu_J + 0.5 * sigma_J**2) - 1
    for t in range(1, STEPS + 1):
        Z = np.random.normal(0, 1)
        N = np.random.poisson(lam * DT)
        J = np.random.lognormal(mu_J, sigma_J) if N > 0 else 1
        if N > 0:
            saltos += N
        prices[t] = prices[t-1] * np.exp((MU - lam * k - 0.5 * sigma**2) * DT + sigma * np.sqrt(DT) * Z) * (J ** N)
    return [round(float(p), 3) for p in prices], saltos


def main():
    data = {"S0": S0, "steps": STEPS, "lambdas": LAMBDAS, "mu_Js": MU_JS,
            "sigma_Js": SIGMA_JS, "sigmas": SIGMAS, "seeds": SEEDS, "trayectorias": {}}
    n = 0
    for lam in LAMBDAS:
        for mu_J in MU_JS:
            for sigma_J in SIGMA_JS:
                for sigma in SIGMAS:
                    key = f"{lam}|{mu_J}|{sigma_J}|{sigma}"
                    series = []
                    for seed in SEEDS:
                        path, saltos = simular(lam, mu_J, sigma_J, sigma, 1000 * seed + int(lam * 100) + int(mu_J * 1000))
                        series.append({"path": path, "saltos": saltos})
                    data["trayectorias"][key] = series
                    n += 1
    out = os.path.join(OUT_DIR, "trayectorias.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, separators=(",", ":"))
    print(f"{n} combinaciones guardadas en {out}")


if __name__ == "__main__":
    main()
