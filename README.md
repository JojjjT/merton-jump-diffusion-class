# Merton Jump-Diffusion — Clase completa

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JojjjT/merton-jump-diffusion-class/blob/main/notebooks/01_colapso_GBM.ipynb)

Clase de 120 minutos sobre **Saltos por Difusión de Merton (1976)** diseñada desde las ciencias cognitivas del aprendizaje: la secuencia produce **conflicto cognitivo** (la intuición de continuidad colapsa) y lo regula con un ciclo **metacognitivo** (Planificar–Monitorear–Controlar–Evaluar).

> **Regla de oro:** la clase no enseña «qué es Merton». Enseña **cómo regular el pensamiento cuando el modelo mental de continuidad colapsa**. Merton es el vehículo; la metacognición es el destino.

🌐 **Sitio web:** <https://jojjjt.github.io/merton-jump-diffusion-class/>

## El proceso

$$\frac{dS_t}{S_t} = (\mu - \lambda k)dt + \sigma dW_t + (J - 1)dN_t$$

- $\lambda$: frecuencia de saltos por año
- $J$: multiplicador del salto (log-normal)
- $k = E[J-1]$: compensación del drift
- $\sigma$: volatilidad de difusión

## Estructura de la clase

| Tiempo | Bloque | Actividad | Recurso |
|---:|---|---|---|
| 0–15 min | 1 | Apertura: «El día que el modelo murió» | `notebooks/01_colapso_GBM.ipynb` |
| 15–45 min | 2 | App interactiva en vivo | `notebooks/02_app_interactiva_merton.ipynb` |
| 45–75 min | 3 | Laboratorio «¿GBM o Merton?» | `docs/hoja_trabajo_gbm_o_merton.pdf` |
| 75–95 min | 4 | Superficie 3D de volatilidad implícita | `notebooks/03_superficie_volatilidad_3D.ipynb` |
| 95–120 min | 5–6 | Juego + debriefing Modelo 3D | `docs/reglas_juego_mercado_que_salta.pdf` |

## Repositorio

```
├── index.html                  # Sitio web (GitHub Pages)
├── docs/                       # PDFs para imprimir
├── notebooks/                  # Cuadernos Colab
├── scripts/                    # App Streamlit + generadores
└── assets/
    ├── laboratorio_graficos/   # 6 PNG (3 GBM, 3 Merton)
    ├── cartas/                 # 20 cartas PNG
    └── debriefing/             # Heatmap de confusión
```

## Uso rápido

### Notebooks en Colab
Abre cualquiera de los tres cuadernos directamente en Google Colab con el botón badge. Solo requieren `numpy`, `matplotlib`, `ipywidgets` y `plotly`.

### Simulador Streamlit
```bash
pip install -r requirements.txt
streamlit run scripts/app_streamlit.py
```

### Regenerar los materiales
```bash
python scripts/generar_graficos_laboratorio.py   # 6 gráficos
python scripts/generar_cartas.py                 # 20 cartas
python scripts/heatmap_debriefing.py             # heatmap (requiere seaborn)
python scripts/generar_pdfs.py                   # DOCX intermedios
python scripts/convertir_docx_a_pdf.py           # conversión a PDF (LibreOffice)
```

## Evaluación

- **Formativa:** tarjeta de regulación metacognitiva + hoja de trabajo
- **Sumativa opcional:** tarea de transferencia (identificar un «salto» real)
- **Rúbrica:** `docs/rubrica_transferencia_metacognitiva.pdf`

## Referencias

1. Merton, R. C. (1976). Option pricing when underlying stock returns are discontinuous. *Journal of Financial Economics*, 3(1-2), 125-144. https://doi.org/10.1016/0304-405X(76)90022-2
2. Wirth, J., et al. (2025). Far transfer of metacognitive regulation. *Educational Psychology Review*.
3. Gobet, F., & Sala, G. (2023). Cognitive training: A field in search of a phenomenon. *Perspectives on Psychological Science*.
4. Kolb, D. A. (1984). *Experiential Learning: Experience as the Source of Learning and Development*.
5. Modelo 3D de Debriefing: Defusing, Discovering, Deepening.

## Licencia

MIT — ver [LICENSE](LICENSE).
