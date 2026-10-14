# Plan de clase: Merton Jump-Diffusion

**Título:** Del conflicto cognitivo a la transferencia metacognitiva  
**Duración:** 120 minutos  
**Nivel:** pregrado/posgrado en finanzas, economía o ingeniería  
**Tecnología necesaria:** proyector, computadores con Google Colab/Python, internet, marcadores, dados y calculadoras. Streamlit es opcional.

## Propósito

La clase no busca que los estudiantes memoricen la ecuación de Merton. Busca que **reconozcan cuándo su modelo mental de continuidad falla** y practiquen regulación metacognitiva para diagnosticar y controlar ese fallo. El proceso de Merton es el vehículo; la metacognición es el destino.

## Objetivos de aprendizaje

Al finalizar la clase, los estudiantes podrán:

1. Explicar por qué el GBM puede describir movimientos suaves pero no eventos de salto.
2. Interpretar los componentes del proceso de Merton: difusión, Poisson, tamaño del salto y compensación del drift.
3. Comparar trayectorias de GBM y Merton usando parámetros controlados.
4. Detectar evidencia visual de saltos en trayectorias de precios.
5. Aplicar el ciclo metacognitivo Planificar–Monitorear–Controlar–Evaluar durante una tarea financiera incierta.
6. Transferir la distinción entre continuidad y discontinuidad a una situación financiera real.

## Marco pedagógico obligatorio

| Principio | Evidencia | Aplicación en la clase |
|---|---|---|
| Conflicto cognitivo | Metaanálisis de cambio conceptual: 218 estudios, N=18.051, **g = 1.10** | La intuición de continuidad debe colapsar al observar un salto inesperado. |
| Regulación metacognitiva | Wirth et al. (2025), N=777 | Cada actividad exige planificar, monitorear, controlar y evaluar. |
| Transferencia lejana | Gobet & Sala (2023) | No se entrena “Merton” como habilidad aislada; se practica regulación aplicable a nuevos problemas. |
| Debriefing estructurado | Modelo 3D: Defusing–Discovering–Deepening, basado en Kolb (1984) | La simulación se convierte en aprendizaje mediante debriefing metacognitivo. |
| Gamificación | Predicción fallida + feedback inmediato | El juego “El Mercado que Salta” hace visible la intuición errónea. |

**Regla de oro:** producir conflicto cognitivo, hacerlo visible y regularlo metacognitivamente.

## Material previo del docente

- Abrir y probar los tres cuadernos Colab antes de la clase.
- Generar los 6 gráficos y las 20 cartas.
- Imprimir la hoja de trabajo, la clave de respuestas, las instrucciones del juego y la tarjeta de regulación.
- Preparar dados y calculadoras para cada mesa.
- Tener una hoja de papel o pizarra para el “mapa de confusión”.
- Verificar que el proyector muestre correctamente las gráficas animadas y la superficie 3D.

## Estructura temporal

| Tiempo | Bloque | Actividad | Recurso principal |
|---:|---|---|---|
| 0–15 min | 1 | Apertura: “El Día que el Modelo Murió” | Cuaderno Colab 01 |
| 15–45 min | 2 | App interactiva en vivo | Cuaderno Colab 02 / app Streamlit |
| 45–75 min | 3 | Laboratorio “¿GBM o Merton?” | Hoja de trabajo + 6 PNG |
| 75–95 min | 4 | Visualización 3D de volatilidad implícita | Cuaderno Colab 03 |
| 95–120 min | 5 y 6 | Juego + debriefing metacognitivo | Cartas + guion de debriefing |

---

## Bloque 1 — Apertura: “El Día que el Modelo Murió” (15 min)

### Intención pedagógica

Romper la expectativa de continuidad antes de explicar la teoría.

### Guion del docente

1. Proyectar una trayectoria suave de GBM.
2. Preguntar: “¿Qué esperan que ocurra en el resto del año?”.
3. Ejecutar la animación hasta el día aproximado 150.
4. Detener en el salto y preguntar: “¿Qué pasó aquí?”.
5. Conectar con Merton (1976): cuando el precio puede saltar, una difusión continua ya no es suficiente.

### Consigna de regulación

- **Planificar:** ¿Qué patrón espero?
- **Monitorear:** ¿Está ocurriendo lo que esperaba?
- **Controlar:** ¿Qué nueva hipótesis formulo?
- **Evaluar:** ¿Qué evidencia me hizo cambiar de opinión?

### Pregunta de salida

“¿Qué información de mercado se pierde si modelamos todos los movimientos como pequeños pasos continuos?”

---

## Bloque 2 — App interactiva en vivo (30 min)

### Intención pedagógica

Permitir que cada estudiante manipule λ, μ_J, σ_J y σ para construir una intuición sobre saltos y difusión.

### Actividad

1. Mostrar la app en el proyector.
2. Pedir predicciones antes de cambiar cada parámetro.
3. Hacer que los estudiantes cambien λ primero, luego μ_J y σ_J.
4. Comparar GBM puro con Merton.
5. Registrar en la tarjeta metacognitiva qué predicciones fueron correctas y cuáles no.

### Preguntas de facilitación

- ¿Qué parámetro controla la probabilidad de observar al menos un salto?
- ¿Qué cambia cuando μ_J es negativo?
- ¿Qué significa que σ_J crezca?
- ¿Por qué una trayectoria sin saltos no prueba que λ=0?

---

## Bloque 3 — Laboratorio “¿GBM o Merton?” (30 min)

### Intención pedagógica

Convertir la percepción en una decisión diagnóstica basada en evidencia.

### Actividad

1. Entregar la hoja de trabajo con 6 gráficos sin parámetros visibles.
2. Cada estudiante clasifica cada trayectoria como GBM o Merton.
3. Anota el día aproximado donde detecta el salto y la razón de su decisión.
4. En parejas, comparan justificaciones.
5. El docente revela la clave solo después de la discusión.

### Extensión opcional

- Calibración por máxima verosimilitud usando JumpDiffSim en R o awt-quant en Python.
- El objetivo no es obtener parámetros perfectos, sino discutir identificabilidad y sensibilidad.

---

## Bloque 4 — Visualización 3D: la sonrisa de volatilidad (20 min)

### Intención pedagógica

Pasar de trayectorias individuales a una consecuencia agregada del modelo: la superficie de volatilidad implícita.

### Actividad

1. Proyectar la superficie 3D interactiva.
2. Cambiar λ y pedir predicciones antes de cada cambio.
3. Rotar la superficie para que los estudiantes identifiquen la “sonrisa”.
4. Conectar el laboratorio de trayectorias con la superficie de precios de opciones.

### Preguntas de discusión

- ¿Dónde se observa mayor volatilidad implícita?
- ¿Cómo cambia la forma cuando aumenta λ?
- ¿Por qué los modelos que ignoran saltos pueden subvalorar colas extremas?

---

## Bloque 5 — Gamificación: “El Mercado que Salta” (25 min)

### Intención pedagógica

Hacer que la intuición de continuidad produzca errores de predicción observables.

### Dinámica

1. Cada mesa comienza con un precio base de 100.
2. Los estudiantes predicen el precio antes de voltear cada carta.
3. Voltean una carta y actualizan el precio.
4. Anotan cada momento en el que la predicción falla.
5. Al final, calculan el precio final con la fórmula simplificada y comparan con la predicción inicial.

### Materiales

- 20 cartas: 17 de difusión y 3 de salto.
- Dados, calculadoras, hoja de predicciones y tarjeta metacognitiva.

---

## Bloque 6 — Debriefing metacognitivo: heatmap de la confusión (20 min)

### Modelo 3D

| Fase | Tiempo | Función | Preguntas guía |
|---|---:|---|---|
| Defusing | 5 min | Reducir activación emocional y hacer explícita la confusión | ¿Qué sentían cuando la predicción falló? ¿Qué frase repitieron para explicar el error? |
| Discovering | 8 min | Descubrir el proceso cognitivo y metacognitivo | ¿En qué momento exacto notaron que su intuición ya no servía? ¿Qué hicieron para corregir? |
| Deepening | 7 min | Transferir a nuevas situaciones | ¿Dónde más ocurren “saltos” en finanzas, economía o vida cotidiana? ¿Qué señal usarían para ajustar su modelo mental? |

### Actividad final

Cada estudiante escribe una frase que empiece con: “Cuando mi modelo mental de continuidad falla, yo…”.

---

## Evaluación

| Tipo | Instrumento | Qué evalúa |
|---|---|---|
| Formativa | Tarjeta de regulación metacognitiva | Planificación, monitoreo, control y evaluación |
| Formativa | Hoja de trabajo | Capacidad de detectar discontinuidades |
| Sumativa opcional | Tarea de transferencia | Aplicación de la distinción en un caso real |
| Reflexiva | Debriefing y frase final | Transferencia metacognitiva |

## Criterios de éxito de la clase

- Los estudiantes pueden explicar por qué un gráfico sugiere saltos.
- Los estudiantes relacionan λ con frecuencia de saltos y μ_J con dirección del salto.
- Los estudiantes identifican al menos un caso real de discontinuidad.
- Los estudiantes usan lenguaje metacognitivo (“esperaba”, “observé”, “ajusté”, “revisé”).

## Adaptaciones

- **Sin Streamlit:** usar el cuaderno Colab con ipywidgets.
- **Sin internet en el aula:** usar el cuaderno descargado con datos precalculados y el PDF del laboratorio.
- **Grupos grandes:** realizar el laboratorio por parejas y el juego por mesas de 4.
- **Tiempo limitado:** recortar la superficie 3D a 10 minutos y mantener el debriefing completo.

## Referencias

- Merton, R. C. (1976). Option pricing when underlying stock returns are discontinuous. *Journal of Financial Economics*, 3(1-2), 125-144. https://doi.org/10.1016/0304-405X(76)90022-2
- Wirth, J., et al. (2025). Far transfer of metacognitive regulation. *Educational Psychology Review*.
- Gobet, F., & Sala, G. (2023). Cognitive training: A field in search of a phenomenon. *Perspectives on Psychological Science*.
- Kolb, D. A. (1984). *Experiential Learning: Experience as the Source of Learning and Development*.
- Modelo 3D de debriefing: Defusing, Discovering, Deepening.
