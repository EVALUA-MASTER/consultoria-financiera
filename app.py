# Corrigiendo y validando app.py para despliegue en Streamlit Cloud con estilo institucional y funcionalidad completa
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import os

st.set_page_config(page_title="Consultoría Financiera Personalizada", layout="wide")

# Estilo institucional
st.markdown("""
    <style>
    body { font-family: 'Segoe UI', sans-serif; background-color:#f5f5f5; }
    h1, h2, h3 { color: #2c3e50; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Consultoría Financiera Personalizada")

# Tabs
tabs = st.tabs(["Cliente", "Patrimonio", "Flujo Mensual", "Riesgos", "Plan de Acción", "Exportar"])

# 1. Registro del cliente
with tabs[0]:
    st.header("🧠 Registro del Cliente")
    nombre = st.text_input("Nombre completo")
    edad = st.number_input("Edad", min_value=0)
    ocupacion = st.text_input("Ocupación")
    ingresos_mensuales = st.number_input("Ingresos mensuales ($)", min_value=0.0)
    objetivos = st.text_area("Objetivos financieros (corto, mediano, largo plazo)")

# 2. Patrimonio neto
with tabs[1]:
    st.header("💰 Patrimonio Neto")
    activos = st.number_input("Total de activos ($)", min_value=0.0)
    pasivos = st.number_input("Total de pasivos ($)", min_value=0.0)
    patrimonio = activos - pasivos
    st.metric("Patrimonio neto", f"${patrimonio:,.2f}")

    if activos > 0 or pasivos > 0:
        fig1, ax1 = plt.subplots()
        ax1.bar(["Activos", "Pasivos"], [activos, pasivos], color=["green", "red"])
        ax1.set_ylabel("Monto ($)")
        st.pyplot(fig1)

# 3. Flujo mensual
with tabs[2]:
    st.header("💸 Flujo Mensual")
    ingresos = st.number_input("Ingresos totales ($)", min_value=0.0)
    gastos = st.number_input("Gastos totales ($)", min_value=0.0)
    ahorro = ingresos - gastos
    st.metric("Ahorro mensual", f"${ahorro:,.2f}")

    if ingresos > 0 or gastos > 0:
        fig2, ax2 = plt.subplots()
        ax2.pie([gastos, ahorro], labels=["Gastos", "Ahorro"], autopct="%1.1f%%", colors=["orange", "blue"])
        st.pyplot(fig2)

# 4. Evaluación de riesgos
with tabs[3]:
    st.header("🚦 Evaluación de Riesgos")
    probabilidad = st.selectbox("Probabilidad del riesgo", ["Alta", "Media", "Baja"])
    impacto = st.selectbox("Impacto del riesgo", ["Alto", "Medio", "Bajo"])

    if probabilidad == "Alta" and impacto == "Alto":
        nivel = "🔴 Alto"
    elif probabilidad == "Media" or impacto == "Medio":
        nivel = "🟠 Medio"
    else:
        nivel = "🟡 Bajo"

    st.subheader(f"Nivel de riesgo: {nivel}")

# 5. Plan de acción
with tabs[4]:
    st.header("📅 Plan Estratégico de Protección")
    plan = pd.DataFrame({
        "Acción": ["Contratar seguro de vida", "Crear fondo de emergencia"],
        "Responsable": ["Cliente", "Cliente"],
        "Fecha": ["2025-11-15", "2025-11-30"],
        "Estado": ["Pendiente", "En proceso"],
        "Observaciones": ["Validar cobertura", "Meta: $1000"]
    })
    st.dataframe(plan)

# 6. Exportar
with tabs[5]:
    st.header("📤 Exportar a Excel")

    def to_excel():
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')

        pd.DataFrame({
            "Nombre": [nombre],
            "Edad": [edad],
            "Ocupación": [ocupacion],
            "Ingresos mensuales": [ingresos_mensuales],
            "Objetivos": [objetivos]
        }).to_excel(writer, sheet_name="Cliente", index=False)

        pd.DataFrame({
            "Activos": [activos],
            "Pasivos": [pasivos],
            "Patrimonio neto": [patrimonio]
        }).to_excel(writer, sheet_name="Patrimonio", index=False)

        pd.DataFrame({
            "Ingresos": [ingresos],
            "Gastos": [gastos],
            "Ahorro": [ahorro]
        }).to_excel(writer, sheet_name="Flujo", index=False)

        pd.DataFrame({
            "Probabilidad": [probabilidad],
            "Impacto": [impacto],
            "Nivel de riesgo": [nivel]
        }).to_excel(writer, sheet_name="Riesgos", index=False)

        plan.to_excel(writer, sheet_name="Plan", index=False)
        writer.close()
        processed_data = output.getvalue()
        return processed_data

    excel_data = to_excel()
    st.download_button("📥 Descargar Excel", data=excel_data, file_name="consultoria_financiera.xlsx")

