import streamlit as st
import numpy as np

# Coeficientes del modelo ajustado con interacción (ldlpost55estimated como outcome)
b0 = 1.3381
b_ldl = -0.0174
b_estat = -0.2687
b_interact = -0.0050
b_edad = 0.0054
b_dm = 0.3206
b_ci = -0.4604

st.set_page_config(page_title="Calculadora de Riesgo LDL < 55")
st.title("Calculator of the probability of LDL-C <55 mg/dl after an ACS")

st.markdown("Required fields.")

# Entradas del usuario
ldl = st.slider("LDL (mg/dL)", min_value=50, max_value=200, value=100)
estatinas = st.radio("¿On-treatment with statins?", [0, 1], format_func=lambda x: "Yes" if x else "No")
edad = st.slider("Age", min_value=18, max_value=100, value=60)
dm = st.radio("¿Diabetes mellitus?", [0, 1], format_func=lambda x: "Yes" if x else "No")
ci = st.radio("¿Previous coronary heart disease?", [0, 1], format_func=lambda x: "Yes" if x else "No")

# Cálculo del logit y probabilidad
interaction = ldl * estatinas
logit = (
    b0 +
    b_ldl * ldl +
    b_estat * estatinas +
    b_interact * interaction +
    b_edad * edad +
    b_dm * dm +
    b_ci * ci
)
prob = 1 / (1 + np.exp(-logit))

# Resultado
st.subheader("Result")
st.metric("Estimated probability of LDLc < 55 mg/dl", f"{prob*100:.1f}%")
