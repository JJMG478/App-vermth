import streamlit as st
import time

# Configuración de página
st.set_page_config(page_title="Ideal Fruits", layout="centered")

# --- ESTILO VISUAL ---
# He ajustado la URL para que encuentre la imagen dentro de tu carpeta
folder_path = "Vermth%20de%20la%20aplicaci%C3%B3n"
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), 
                    url("https://raw.githubusercontent.com/JJMG478/App-vermth/main/{folder_path}/1758951782602.jpg");
        background-size: cover;
        background-position: center;
    }}
    .stButton > button {{
        width: 100%; height: 80px; font-size: 22px !important;
        font-weight: bold; border-radius: 15px; margin-bottom: 15px;
        color: white; border: none; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }}
    div.stButton:nth-child(3) > button {{ background-color: #2e4a7d; }}
    div.stButton:nth-child(4) > button {{ background-color: #3e5c3e; }}
    div.stButton:nth-child(5) > button {{ background-color: #d17a2d; }}
    div.stButton:nth-child(6) > button {{ background-color: #8b2626; }}
    </style>
""", unsafe_allow_html=True)

# --- PANTALLA DE CARGA ---
if 'cargado' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        st.image("Vermth de la aplicación/Logotipo-ideal-fruits.png", use_container_width=True)
        st.markdown("<h2 style='text-align: center;'>Cargando Ideal Fruits...</h2>", unsafe_allow_html=True)
        time.sleep(4)
    st.session_state.cargado = True
    placeholder.empty()

# --- NAVEGACIÓN ---
if 'seccion' not in st.session_state:
    st.session_state.seccion = 'menu'

# --- MENÚ PRINCIPAL ---
if st.session_state.seccion == 'menu':
    st.image("Vermth de la aplicación/Logotipo-ideal-fruits.png", width=150)
    
    if st.button("1. Gestionar Nuevo Pedido"):
        st.session_state.seccion = 'pedido'
        st.rerun()
    
    st.button("2. Ver Stocks y Costes Actuales")
    st.button("3. Ajustar Stocks, Costes y Tarifas")
    
    if st.button("4. Salir"):
        st.session_state.clear()
        st.rerun()

# --- SECCIÓN 1: NUEVO PEDIDO ---
elif st.session_state.seccion == 'pedido':
    st.header("🛒 Nuevo Pedido")
    if st.button("⬅️ Volver al Menú"):
        st.session_state.seccion = 'menu'
        st.rerun()
    
    cliente = st.text_input("Nombre del Cliente")
    formato = st.selectbox("Formato", ["75cl", "25cl"])
    cantidad = st.number_input("Cantidad de botellas", min_value=1, step=1)
    
    if st.button("Confirmar Pedido"):
        st.success(f"Pedido de {cantidad} botellas para {cliente} registrado (Simulación)")
