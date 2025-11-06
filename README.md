![Escudo Institucional](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Coat_of_arms_of_Ecuador.svg/120px-Coat_of_arms_of_Ecuador.svg.png)

# Consultoría Financiera Personalizada

Aplicación web desarrollada para brindar asesoría financiera clara, visual y estratégica a clientes institucionales y familiares. Permite registrar datos clave, evaluar patrimonio, flujo mensual, riesgos y generar un plan de acción exportable a Excel.

---

## 📋 Tabla de contenido

- [Características](#características)
- [Capturas de pantalla](#capturas-de-pantalla)
- [Guía de uso](#guía-de-uso)
- [Despliegue en Streamlit Cloud](#despliegue-en-streamlit-cloud)
- [Requisitos técnicos](#requisitos-técnicos)
- [Créditos](#créditos)
- [Licencia](#licencia)

---

## ✨ Características

- Registro de cliente con datos clave
- Evaluación de patrimonio neto (activos vs pasivos)
- Flujo mensual con cálculo de ahorro
- Semáforo de riesgos (probabilidad e impacto)
- Plan de acción editable
- Exportación a Excel con hojas separadas
- Interfaz visual clara y profesional

---

## 🖼️ Capturas de pantalla

> *(Puedes agregar imágenes aquí desde tu app desplegada)*  
> Ejemplo:  
> ![Interfaz principal](https://via.placeholder.com/600x300.png?text=Consultoria+Financiera)

---

## 🧭 Guía de uso

1. Ingresa los datos del cliente
2. Registra activos y pasivos para calcular patrimonio
3. Introduce ingresos y gastos mensuales
4. Evalúa riesgos con probabilidad e impacto
5. Define un plan de acción personalizado
6. Haz clic en **Exportar a Excel** para generar el informe

---

## 🚀 Despliegue en Streamlit Cloud

Para desplegar esta app:

1. Ve a [streamlit.io/cloud](https://streamlit.io/cloud)
2. Inicia sesión con tu cuenta de GitHub
3. Llena los campos:

| Campo | Valor |
|-------|-------|
| Repositorio | `EVALUA-MASTER/consultoria-financiera` |
| Rama | `main` |
| Archivo principal | `app.py` |

4. Haz clic en **Desplegar**

---

## ⚙️ Requisitos técnicos

- Python 3.10+
- Streamlit
- Pandas
- Matplotlib
- XlsxWriter

Instalación local:

```bash
pip install -r requirements.txt
streamlit run app.py

