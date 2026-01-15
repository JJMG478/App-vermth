import streamlit as st
import time

# Configuración de página
st.set_page_config(page_title="Ideal Fruits", layout="centered")

# Ruta de la carpeta en GitHub
folder = "Vermth%20de%20la%20aplicaci%C3%B3n"

# Estilo visual: Fondo corregido
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), 
                    url("https://raw.githubusercontent.com/JJMG478/App-vermth/principal/{folder}/1758951782602.jpg");
        background-size: cover;
        background-position: center;
    }}
    .stButton > button {{
        width: 100%;
        height: 80px;
        font-size: 22px !important;
        font-weight: bold;
        border-radius: 15px;
        margin-bottom: 15px;
        color: white;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }}
    div.stButton:nth-child(3) > button {{ background-color: #2e4a7d; }}
    div.stButton:nth-child(4) > button {{ background-color: #3e5c3e; }}
    div.stButton:nth-child(5) > button {{ background-color: #d17a2d; }}
    div.stButton:nth-child(6) > button {{ background-color: #8b2626; }}
    </style>
""", unsafe_allow_html=True)

# Pantalla de carga corregida
if 'cargado' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        st.image("Vermth de la aplicación/Logotipo-ideal-fruits.png", use_container_width=True)
        st.markdown("<h2 style='text-align: center;'>Cargando Ideal Fruits...</h2>", unsafe_allow_html=True)
        time.sleep(4)
    st.session_state.cargado = True
    placeholder.empty()

# Menú Principal corregido
st.image("Vermth de la aplicación/Logotipo-ideal-fruits.png", width=150)
st.button("1. Gestionar Nuevo Pedido")
st.button("2. Ver Stocks y Costes Actuales")
st.button("3. Ajustar Stocks, Costes y Tarifas")
st.button("4. Salir")
