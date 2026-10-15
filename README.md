# Saltos por Difusión de Merton — sitio de clase

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JojjjT/merton-jump-diffusion-class/blob/main/notebooks/01_colapso_GBM.ipynb)

Recurso de estudio de **120 minutos** sobre el proceso de saltos por difusión de Merton (1976): teoría, simulaciones interactivas en el navegador, laboratorio de detección de saltos y material para clase.

🌐 **Sitio web:** <https://jojjjt.github.io/merton-jump-diffusion-class/>

## El proceso

$$\frac{dS_t}{S_t} = (\mu - \lambda k)dt + \sigma dW_t + (J - 1)dN_t$$

- $\lambda$: frecuencia de saltos por año
- $J$: multiplicador del salto (log-normal)
- $k = E[J-1]$: compensación del drift
- $\sigma$: volatilidad de difusión

## Estructura de la clase

| Tiempo | Bloque | Actividad |
|---:|---|---|
| 0–15 min | 1 | Apertura: trayectoria con salto abrupto |
| 15–45 min | 2 | Simulación interactiva de parámetros |
| 45–75 min | 3 | Laboratorio "¿GBM o Merton?" |
| 75–95 min | 4 | Volatilidad implícita y sonrisa |
| 95–120 min | 5–6 | Juego de predicción + cierre |

## Repositorio

Sitio construido con [Quarto](https://quarto.org). El HTML se genera en cada push mediante GitHub Actions y se publica en GitHub Pages.

```
├── _quarto.yml                  # Config del sitio (navbar, sidebar, tema)
├── index.qmd                    # Landing
├── teoria.qmd                   # Proceso de Merton (ecuación LaTeX)
├── herramientas.qmd             # 4 simuladores interactivos (JS puro)
├── demo_trayectorias.qmd        # Demo plotly con slider de λ
├── materiales.qmd               # PDFs + galería de cartas/gráficos
├── slides/                      # 5 presentaciones revealjs
├── styles/
│   ├── custom.scss              # Sistema de diseño (blanco y negro)
│   ├── reveal-merton.scss       # Tema de presentaciones
│   ├── animations.css           # Motion CSS puro
│   └── inject.html              # Fuentes + IntersectionObserver
├── data/trayectorias.json       # Trayectorias precalculadas
├── notebooks/                   # 3 cuadernos .ipynb (Colab + Quarto)
├── docs/                        # PDFs para imprimir
├── scripts/                     # Streamlit + generadores
├── assets/                      # PNG (gráficos, cartas)
└── .github/workflows/publish.yml  # Deploy automático a Pages
```

## Uso rápido

### Ver el sitio en local
```bash
quarto preview
```

### Construir el sitio
```bash
quarto render          # genera _site/
```

### Notebooks en Colab
Abre cualquiera de los tres cuadernos directamente en Google Colab con el botón badge. Solo requieren `numpy`, `matplotlib`, `ipywidgets` y `plotly`.

### Simulador Streamlit
```bash
pip install -r requirements.txt
streamlit run scripts/app_streamlit.py
```

### Herramientas interactivas
Cuatro simuladores en JavaScript puro que corren en el navegador sin servidor: Monte Carlo de trayectorias, distribución de retornos GBM vs Merton, precios de opciones Merton vs Black-Scholes y proceso de Poisson.

### Regenerar los materiales
```bash
python scripts/generar_graficos_laboratorio.py   # 6 gráficos
python scripts/generar_cartas.py                 # 20 cartas
python scripts/precalcular_trayectorias.py       # data/trayectorias.json
python scripts/generar_pdfs.py                   # DOCX intermedios
python scripts/convertir_docx_a_pdf.py           # conversión a PDF (LibreOffice)
```

### Publicación
Cada push a `main` ejecuta `.github/workflows/publish.yml`: instala Quarto, ejecuta `quarto render` y despliega `_site/` a GitHub Pages.

## Materiales

- **Hoja de trabajo** y **clave de respuestas**: `docs/`
- **Reglas del juego**: `docs/`
- **Agenda de clase**: `docs/`
- **Presentaciones**: sección "Presentaciones" del sitio

## Referencias

1. Merton, R. C. (1976). Option pricing when underlying stock returns are discontinuous. *Journal of Financial Economics*, 3(1-2), 125-144.
2. Black, F., & Scholes, M. (1973). The pricing of options and corporate liabilities. *Journal of Political Economy*, 81(3), 637–654.
3. Bakshi, G., Kapadia, N., & Madan, D. (2003). Stock return characteristics, skewness, and the pricing of option claims. *Journal of Financial Economics*, 69(1), 3–41.

## Licencia

MIT — ver [LICENSE](LICENSE).
