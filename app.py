# Corrigiendo app.py para evitar errores de matplotlib con datos no numéricos o vacíos
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# Estilo institucional
st.set_page_config(page_title="Consultoría Financiera", layout="wide")
st.title("🧭 Consultoría Financiera Personalizada")

# Función para validar y convertir datos numéricos
def safe_numeric_conversion(series):
    return pd.to_numeric(series, errors='coerce').fillna(0)

# Pestaña 1: Registro del cliente
with st.expander("📋 Registro del Cliente"):
    nombre = st.text_input("Nombre completo")
    edad = st.number_input("Edad", min_value=0, max_value=120)
    correo = st.text_input("Correo electrónico")
    telefono = st.text_input("Teléfono")
    ciudad = st.text_input("Ciudad")

# Pestaña 2: Patrimonio neto
with st.expander("💰 Patrimonio Neto"):
    st.write("Ingresa tus activos y pasivos:")
    activos = st.text_area("Activos (separados por coma)", "Casa,Auto,Ahorros")
    valores_activos = st.text_area("Valores de activos", "80000,15000,10000")
    pasivos = st.text_area("Pasivos (separados por coma)", "Hipoteca,Deuda Auto")
    valores_pasivos = st.text_area("Valores de pasivos", "50000,10000")

    activos_lista = [x.strip() for x in activos.split(",")]
    valores_activos_lista = safe_numeric_conversion(pd.Series(valores_activos.split(",")))
    pasivos_lista = [x.strip() for x in pasivos.split(",")]
    valores_pasivos_lista = safe_numeric_conversion(pd.Series(valores_pasivos.split(",")))

    patrimonio = valores_activos_lista.sum() - valores_pasivos_lista.sum()
    st.metric("Patrimonio Neto", f"${patrimonio:,.2f}")

    if len(activos_lista) == len(valores_activos_lista) and not valores_activos_lista.empty:
        fig1, ax1 = plt.subplots()
        ax1.bar(activos_lista, valores_activos_lista, color='green')
        ax1.set_title("Activos")
        st.pyplot(fig1)

    if len(pasivos_lista) == len(valores_pasivos_lista) and not valores_pasivos_lista.empty:
        fig2, ax2 = plt.subplots()
        ax2.bar(pasivos_lista, valores_pasivos_lista, color='red')
        ax2.set_title("Pasivos")
        st.pyplot(fig2)

# Pestaña 3: Flujo mensual
with st.expander("📊 Flujo Mensual"):
    ingresos = st.text_input("Ingresos mensuales", "2000")
    gastos = st.text_input("Gastos mensuales", "1500")

    ingresos_val = pd.to_numeric(ingresos, errors='coerce')
    gastos_val = pd.to_numeric(gastos, errors='coerce')

    if not np.isnan(ingresos_val) and not np.isnan(gastos_val):
        ahorro = ingresos_val - gastos_val
        st.metric("Ahorro mensual", f"${ahorro:,.2f}")

        fig3, ax3 = plt.subplots()
        ax3.pie([ingresos_val, gastos_val], labels=["Ingresos", "Gastos"], autopct='%1.1f%%', colors=["blue", "orange"])
        ax3.set_title("Distribución mensual")
        st.pyplot(fig3)

# Pestaña 4: Evaluación de riesgos
with st.expander("🚦 Evaluación de Riesgos"):
    riesgo_credito = st.slider("Riesgo de crédito", 0, 100, 30)
    riesgo_liquidez = st.slider("Riesgo de liquidez", 0, 100, 50)
    riesgo_mercado = st.slider("Riesgo de mercado", 0, 100, 70)

    fig4, ax4 = plt.subplots()
    riesgos = ["Crédito", "Liquidez", "Mercado"]
    valores_riesgo = [riesgo_credito, riesgo_liquidez, riesgo_mercado]
    colores = ['green' if v < 40 else 'orange' if v < 70 else 'red' for v in valores_riesgo]
    ax4.bar(riesgos, valores_riesgo, color=colores)
    ax4.set_ylim(0, 100)
    ax4.set_title("Semáforo de Riesgos")
    st.pyplot(fig4)

# Pestaña 5: Plan de acción
with st.expander("📝 Plan de Acción"):
    plan = st.text_area("Escribe tu plan financiero personalizado aquí")

# Exportar a Excel
if st.button("📤 Exportar a Excel"):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    df_cliente = pd.DataFrame({
        "Campo": ["Nombre", "Edad", "Correo", "Teléfono", "Ciudad"],
        "Valor": [nombre, edad, correo, telefono, ciudad]
    })
    df_activos = pd.DataFrame({"Activo": activos_lista, "Valor": valores_activos_lista})
    df_pasivos = pd.DataFrame({"Pasivo": pasivos_lista, "Valor": valores_pasivos_lista})
    df_flujo = pd.DataFrame({"Ingresos": [ingresos_val], "Gastos": [gastos_val], "Ahorro": [ahorro]})
    df_riesgos = pd.DataFrame({"Tipo": riesgos, "Valor": valores_riesgo})
    df_plan = pd.DataFrame({"Plan": [plan]})

    df_cliente.to_excel(writer, sheet_name="Cliente", index=False)
    df_activos.to_excel(writer, sheet_name="Activos", index=False)
    df_pasivos.to_excel(writer, sheet_name="Pasivos", index=False)
    df_flujo.to_excel(writer, sheet_name="Flujo", index=False)
    df_riesgos.to_excel(writer, sheet_name="Riesgos", index=False)
    df_plan.to_excel(writer, sheet_name="Plan", index=False)

    writer.save()
    output.seek(0)
    st.download_button("📥 Descargar Excel", data=output, file_name="consultoria_financiera.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

