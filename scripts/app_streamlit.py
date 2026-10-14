"""
App Streamlit para simular Merton Jump-Diffusion.
Ejecutar: streamlit run scripts/app_streamlit.py
"""
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Merton Jump-Diffusion", layout="wide")
st.title("Simulador Merton Jump-Diffusion")
st.markdown(
    r"""
Proceso de Merton (1976):

$$\frac{dS_t}{S_t} = (\mu - \lambda k)dt + \sigma dW_t + (J - 1)dN_t$$
"""
)

col1, col2, col3, col4 = st.columns(4)
lam = col1.slider("λ (saltos/año)", 0.0, 5.0, 1.0, 0.1)
mu_J = col2.slider("μ_J (media del log del salto)", -0.3, 0.3, -0.08, 0.01)
sigma_J = col3.slider("σ_J (volatilidad del salto)", 0.0, 0.3, 0.12, 0.01)
sigma = col4.slider("σ (difusión)", 0.1, 0.5, 0.2, 0.01)

mu = st.slider("μ (drift)", 0.01, 0.15, 0.05, 0.01)
steps = st.slider("Pasos (días)", 100, 500, 252, 1)
n_trayectorias = st.slider("Número de trayectorias", 1, 20, 1)

if st.button("Generar nueva trayectoria"):
    st.session_state["seed"] = int(np.random.randint(0, 100000))

seed = st.session_state.get("seed", 42)
np.random.seed(seed)
dt = 1.0 / steps

fig, ax = plt.subplots(figsize=(12, 5))
saltos_totales = 0
for _ in range(n_trayectorias):
    prices = np.zeros(steps + 1)
    prices[0] = 100
    for t in range(1, steps + 1):
        Z = np.random.normal(0, 1)
        N = np.random.poisson(lam * dt)
        J = np.random.lognormal(mu_J, sigma_J) if N > 0 else 1
        prices[t] = prices[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z) * (J ** N)
        saltos_totales += N
    ax.plot(prices, alpha=0.6)

ax.axhline(100, color="gray", linestyle="--", alpha=0.4)
ax.set_xlabel("Días")
ax.set_ylabel("Precio")
ax.set_title(f"λ={lam:.1f} | μ_J={mu_J:.2f} | σ_J={sigma_J:.2f} | σ={sigma:.2f} | Saltos: {saltos_totales}")
ax.grid(alpha=0.3)
st.pyplot(fig)

st.info(f"**Total de saltos observados:** {saltos_totales}")
st.caption("Adaptado de Merton (1976).")
