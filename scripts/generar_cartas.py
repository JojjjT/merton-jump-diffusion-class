"""
Genera 20 cartas PNG para el juego 'El Mercado que Salta' (blanco y negro):
- 17 cartas de difusión (fondo blanco, borde negro)
- 3 cartas de salto (fondo negro, texto blanco)
"""
import os
import textwrap
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE, "assets", "cartas")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generar_carta(tipo, numero, movimiento, descripcion):
    fig, ax = plt.subplots(figsize=(3, 4.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    if tipo == "difusion":
        # Fondo blanco, borde negro
        face, edge, ink = "#ffffff", "#000000", "#000000"
    else:
        # Inversión: fondo negro, texto blanco
        face, edge, ink = "#000000", "#000000", "#ffffff"

    ax.add_patch(Rectangle((0.05, 0.05), 0.9, 0.9, facecolor=face, edgecolor=edge, lw=3))
    ax.text(0.5, 0.78, f"CARTA {numero}", ha="center", fontsize=14, fontweight="bold", color=ink)
    ax.text(0.5, 0.55, movimiento, ha="center", fontsize=22, fontweight="bold", color=ink)
    # Descripción con ajuste de línea para que no desborde el rectángulo
    wrapped = "\n".join(textwrap.wrap(descripcion, width=26))
    ax.text(0.5, 0.36, wrapped, ha="center", va="top", fontsize=8.5,
            color=ink, linespacing=1.4)
    ax.text(0.5, 0.09, tipo.upper(), ha="center", fontsize=12, style="italic", color=ink)
    ax.axis("off")
    plt.savefig(os.path.join(OUTPUT_DIR, f"carta_{tipo}_{numero}.png"), dpi=150, bbox_inches="tight")
    plt.close()

# 17 cartas de difusión
for i in range(1, 18):
    generar_carta("difusion", i, "±2%", "Tira el dado. Si sale 1-3, sube 2%. Si sale 4-6, baja 2%.")

# 3 cartas de salto
for i in range(1, 4):
    generar_carta("salto", i, "-15%", "¡SALTO! El precio cae 15%.")

print(f"20 cartas (B/N) guardadas en {OUTPUT_DIR}")
