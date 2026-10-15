# Agenda de clase: Saltos por Difusión de Merton

**Título:** Saltos por Difusión de Merton — teoría, simulaciones y material de clase
**Duración:** 120 minutos
**Nivel:** pregrado/posgrado en finanzas, economía o ingeniería
**Tecnología necesaria:** proyector, computadores con Google Colab/Python, internet, marcadores, dados y calculadoras. Streamlit es opcional.

## Propósito

Comprender y aplicar el proceso de saltos por difusión de Merton (1976): modelar precios que se mueven de forma continua **y** de vez en cuando saltan. La clase combina teoría, simulación interactiva y práctica de detección de saltos.

## Objetivos de aprendizaje

Al finalizar la clase, los estudiantes podrán:

1. Explicar por qué el GBM describe movimientos suaves pero no eventos de salto.
2. Interpretar los componentes del proceso de Merton: difusión, Poisson, tamaño del salto y compensación del drift.
3. Comparar trayectorias de GBM y Merton usando parámetros controlados.
4. Detectar evidencia visual de saltos en trayectorias de precios.
5. Relacionar los saltos con la volatilidad implícita y la sonrisa de precios de opciones.
6. Aplicar la distinción entre continuidad y discontinuidad a una situación financiera real.

## Conceptos clave de la clase

| # | Concepto | Definición breve |
|---|---|---|
| 1 | Difusión continua vs. salto discontinuo | La difusión nunca mueve el precio de golpe; el salto, sí |
| 2 | Proceso de Poisson | Genera los instantes de salto con frecuencia λ |
| 3 | Log-normalidad del salto | El multiplicador J > 0, con media μ_J y desviación σ_J |
| 4 | Compensación del drift (λk) | Si los saltos pueden ser negativos, el drift se ajusta |
| 5 | Volatilidad implícita | Los modelos de saltos producen la "sonrisa" que Black-Scholes ignora |
| 6 | Calibración por máxima verosimilitud | Estimar λ, μ_J, σ_J y σ a partir de datos |

## Material previo del docente

- Abrir y probar los tres cuadernos Colab antes de la clase.
- Generar los 6 gráficos y las 20 cartas.
- Imprimir la hoja de trabajo, la clave de respuestas y las instrucciones del juego.
- Preparar dados y calculadoras para cada mesa.
- Verificar que el proyector muestre correctamente las gráficas animadas y la superficie 3D.

## Estructura temporal

| Tiempo | Bloque | Actividad | Recurso principal |
|---:|---|---|---|
| 0–15 min | 1 | Apertura: trayectoria con salto abrupto | Cuaderno Colab 01 |
| 15–45 min | 2 | Simulación interactiva de parámetros | Cuaderno Colab 02 / app Streamlit / Herramientas |
| 45–75 min | 3 | Laboratorio "¿GBM o Merton?" | Hoja de trabajo + 6 PNG |
| 75–95 min | 4 | Volatilidad implícita: la sonrisa | Cuaderno Colab 03 |
| 95–120 min | 5 y 6 | Juego de predicción + cierre | Cartas + agenda |

---

## Bloque 1 — Apertura: trayectoria con salto (15 min)

**Objetivo:** mostrar una discontinuidad en un precio antes de explicar la teoría.

### Guion del docente

1. Proyectar una trayectoria suave de GBM.
2. Preguntar: "¿Qué esperan que ocurra en el resto del año?".
3. Ejecutar la animación hasta el día aproximado 150.
4. Detener en el salto y preguntar: "¿Qué pasó aquí?".
5. Conectar con Merton (1976): cuando el precio puede saltar, una difusión continua ya no es suficiente.

### Pregunta de salida

"¿Qué información de mercado se pierde si modelamos todos los movimientos como pequeños pasos continuos?"

---

## Bloque 2 — Simulación interactiva en vivo (30 min)

**Objetivo:** manipular λ, μ_J, σ_J y σ para construir una intuición sobre saltos y difusión.

### Actividad

1. Mostrar la simulación en el proyector (app o página de Herramientas).
2. Pedir predicciones antes de cambiar cada parámetro.
3. Cambiar λ primero, luego μ_J y σ_J.
4. Comparar GBM puro con Merton.
5. Registrar qué predicciones fueron correctas y cuáles no.

### Preguntas de facilitación

- ¿Qué parámetro controla la probabilidad de observar al menos un salto?
- ¿Qué cambia cuando μ_J es negativo?
- ¿Qué significa que σ_J crezca?
- ¿Por qué una trayectoria sin saltos no prueba que λ=0?

---

## Bloque 3 — Laboratorio "¿GBM o Merton?" (30 min)

**Objetivo:** convertir la percepción en una decisión diagnóstica basada en evidencia.

### Actividad

1. Entregar la hoja de trabajo con 6 gráficos sin parámetros visibles.
2. Cada estudiante clasifica cada trayectoria como GBM o Merton.
3. Anota el día aproximado donde detecta el salto y la razón de su decisión.
4. En parejas, comparan justificaciones.
5. El docente revela la clave solo después de la discusión.

### Extensión opcional

- Calibración por máxima verosimilitud usando JumpDiffSim en R o librerías cuantitativas en Python.
- El objetivo no es obtener parámetros perfectos, sino discutir identificabilidad y sensibilidad.

---

## Bloque 4 — Visualización 3D: la sonrisa de volatilidad (20 min)

**Objetivo:** pasar de trayectorias individuales a una consecuencia agregada del modelo: la superficie de volatilidad implícita.

### Actividad

1. Proyectar la superficie 3D interactiva.
2. Cambiar λ y pedir predicciones antes de cada cambio.
3. Rotar la superficie para identificar la "sonrisa".
4. Conectar el laboratorio de trayectorias con la superficie de precios de opciones.

### Preguntas de discusión

- ¿Dónde se observa mayor volatilidad implícita?
- ¿Cómo cambia la forma cuando aumenta λ?
- ¿Por qué los modelos que ignoran saltos pueden subvalorar colas extremas?

---

## Bloque 5 — Juego: "El Mercado que Salta" (25 min)

**Objetivo:** experimentar con números el efecto de los saltos sobre un precio.

### Dinámica

1. Cada mesa comienza con un precio base de 100.
2. Los estudiantes predicen el precio antes de voltear cada carta.
3. Voltean una carta y actualizan el precio.
4. Anotan cada momento en el que la predicción falla.
5. Al final, calculan el precio final con la fórmula simplificada y comparan con la predicción inicial.

### Materiales

- 20 cartas: 17 de difusión y 3 de salto.
- Dados, calculadoras y hoja de predicciones.

---

## Bloque 6 — Cierre y síntesis (20 min)

### Síntesis de la clase

- El GBM asume continuidad; los mercatos saltan.
- Merton agrega un proceso de Poisson con frecuencia λ.
- Los saltos se ven en trayectorias, en la sonrisa de volatilidad y en los precios de opciones.

### Actividad final

Cada estudiante identifica un "salto" real (financiero o económico) y describe cómo lo modelaría con los parámetros del proceso.

---

## Evaluación

| Tipo | Instrumento | Qué evalúa |
|---|---|---|
| Formativa | Hoja de trabajo | Capacidad de detectar discontinuidades |
| Formativa | Predicciones en la demo | Manipulación correcta de los parámetros |
| Sumativa opcional | Taller: un salto en la vida real | Aplicación de la distinción en un caso real |

## Criterios de éxito de la clase

- Los estudiantes pueden explicar por qué un gráfico sugiere saltos.
- Los estudiantes relacionan λ con frecuencia de saltos y μ_J con dirección del salto.
- Los estudiantes identifican al menos un caso real de discontinuidad.
- Los estudiantes interpretan la sonrisa de volatilidad implícita.

## Adaptaciones

- **Sin Streamlit:** usar el cuaderno Colab con ipywidgets o las herramientas del sitio.
- **Sin internet en el aula:** usar el cuaderno descargado con datos precalculados y el PDF del laboratorio.
- **Grupos grandes:** realizar el laboratorio por parejas y el juego por mesas de 4.
- **Tiempo limitado:** recortar la superficie 3D a 10 minutos y mantener el cierre.

## Referencias

- Merton, R. C. (1976). Option pricing when underlying stock returns are discontinuous. *Journal of Financial Economics*, 3(1-2), 125-144. https://doi.org/10.1016/0304-405X(76)90022-2
- Black, F., & Scholes, M. (1973). The pricing of options and corporate liabilities. *Journal of Political Economy*, 81(3), 637–654.
