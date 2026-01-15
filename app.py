import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Ideal Fruits", layout="centered")

# Estilo visual (Botella de fondo y botones grandes)
folder_path = "Vermth%20de%20la%20aplicaci%C3%B3n"
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)), 
                    url("https://raw.githubusercontent.com/JJMG478/App-vermth/main/{folder_path}/1758951782602.jpg");
        background-size: cover;
    }}
    .stButton > button {{
        width: 100%; height: 70px; font-size: 20px !important;
        font-weight: bold; border-radius: 12px; margin-bottom: 10px;
        color: white; border: none;
    }}
    div.stButton:nth-child(3) > button {{ background-color: #2e4a7d; }}
    div.stButton:nth-child(4) > button {{ background-color: #3e5c3e; }}
    div.stButton:nth-child(5) > button {{ background-color: #d17a2d; }}
    div.stButton:nth-child(6) > button {{ background-color: #8b2626; }}
    </style>
""", unsafe_allow_html=True)

# Base de datos temporal (en la sesión del móvil)
if 'historial_ventas' not in st.session_state:
    st.session_state.historial_ventas = []

# --- NAVEGACIÓN ---
if 'seccion' not in st.session_state:
    st.session_state.seccion = 'menu'

# --- MENÚ PRINCIPAL ---
if st.session_state.seccion == 'menu':
    st.image("Vermth de la aplicación/Logotipo-ideal-fruits.png", width=120)
    st.title("Ideal Fruits - Gestión")
    
    if st.button("🛒 1. Gestionar Nuevo Pedido"):
        st.session_state.seccion = 'pedido'
        st.rerun()
    
    if st.button("📦 2. Ver Resumen de Ventas"):
        st.session_state.seccion = 'resumen'
        st.rerun()
        
    st.button("⚙️ 3. Ajustar Tarifas (Próximamente)")
    
    if st.button("❌ 4. Salir"):
        st.session_state.clear()
        st.rerun()

# --- SECCIÓN: NUEVO PEDIDO ---
elif st.session_state.seccion == 'pedido':
    st.header("Nuevo Pedido")
    if st.button("⬅️ Volver"):
        st.session_state.seccion = 'menu'
        st.rerun()
        
    with st.form("venta"):
        cliente = st.text_input("Nombre Cliente")
        formato = st.selectbox("Formato", ["75cl", "25cl"])
        tipo = st.selectbox("Tipo", ["Distribuidor", "Horeca", "Particular"])
        cantidad = st.number_input("Botellas", min_value=1, value=6)
        precio = st.number_input("Precio Unitario (€)", value=12.0)
        
        if st.form_submit_button("✅ REGISTRAR VENTA"):
            nueva_venta = {
                "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": cliente,
                "Formato": formato,
                "Cantidad": cantidad,
                "Total": cantidad * precio
            }
            st.session_state.historial_ventas.append(nueva_venta)
            st.success("¡Venta guardada con éxito!")
            time.sleep(1)
            st.session_state.seccion = 'menu'
            st.rerun()

# --- SECCIÓN: RESUMEN ---
elif st.session_state.seccion == 'resumen':
    st.header("📊 Resumen de Hoy")
    if st.button("⬅️ Volver"):
        st.session_state.seccion = 'menu'
        st.rerun()
    
    if st.session_state.historial_ventas:
        df = pd.DataFrame(st.session_state.historial_ventas)
        st.table(df)
        st.write(f"**Total Recaudado: {df['Total'].sum():.2f}€**")
    else:
        st.warning("No hay ventas registradas todavía.")
