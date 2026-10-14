"""
Genera 20 cartas PNG para el juego 'El Mercado que Salta':
- 17 cartas de difusión
- 3 cartas de salto
"""
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE, "assets", "cartas")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generar_carta(tipo, numero, movimiento, descripcion):
    fig, ax = plt.subplots(figsize=(3, 4.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    color = "#2ecc71" if tipo == "difusion" else "#e74c3c"
    ax.add_patch(Rectangle((0.05, 0.05), 0.9, 0.9, facecolor=color, alpha=0.2, edgecolor=color, lw=3))
    ax.text(0.5, 0.78, f"CARTA {numero}", ha="center", fontsize=14, fontweight="bold")
    ax.text(0.5, 0.55, movimiento, ha="center", fontsize=22, fontweight="bold", color=color)
    ax.text(0.5, 0.25, descripcion, ha="center", fontsize=10, wrap=True)
    ax.text(0.5, 0.10, tipo.upper(), ha="center", fontsize=12, style="italic")
    ax.axis("off")
    plt.savefig(os.path.join(OUTPUT_DIR, f"carta_{tipo}_{numero}.png"), dpi=150, bbox_inches="tight")
    plt.close()

# 17 cartas de difusión
for i in range(1, 18):
    generar_carta("difusion", i, "±2%", "Tira el dado. Si sale 1-3, sube 2%. Si sale 4-6, baja 2%.")

# 3 cartas de salto
for i in range(1, 4):
    generar_carta("salto", i, "-15%", "¡SALTO! El precio cae 15%.")

print(f"20 cartas guardadas en {OUTPUT_DIR}")
