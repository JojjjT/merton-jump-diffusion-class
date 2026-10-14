"""
Genera el heatmap del debriefing metacognitivo.
Reemplaza las frecuencias simuladas con los datos reales del formulario.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE, "assets", "debriefing")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Datos simulados (reemplazar con respuestas reales del formulario)
data = {
    "Momento": ["Animación", "App λ", "Laboratorio", "Calibración", "Juego", "Superficie 3D"],
    "Frecuencia": [25, 18, 30, 12, 35, 10],
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))
sns.barplot(x="Momento", y="Frecuencia", data=df, palette="Reds_r")
plt.title("¿En qué momento falló tu intuición de continuidad?", fontsize=14)
plt.ylabel("Número de estudiantes")
plt.xlabel("")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "heatmap_confusion.png"), dpi=150, bbox_inches="tight")
plt.close()
