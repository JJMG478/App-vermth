import streamlit as st
import time

# Configuración de página
st.set_page_config(page_title="Ideal Fruits", layout="centered")

# --- ESTILO VISUAL ---
folder_path = "Vermth%20de%20la%20aplicaci%C3%B3n"
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)), 
                    url("https://raw.githubusercontent.com/JJMG478/App-vermth/main/{folder_path}/1758951782602.jpg");
        background-size: cover;
        background-position: center;
    }}
    .stButton > button {{
        width: 100%; height: 70px; font-size: 20px !important;
        font-weight: bold; border-radius: 12px; margin-bottom: 10px;
        color: white; border: none;
    }}
    /* Colores de los botones del menú */
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
        time.sleep(4)
    st.session_state.cargado = True
    placeholder.empty()

# --- INICIALIZACIÓN DE DATOS ---
if 'seccion' not in st.session_state:
    st.session_state.seccion = 'menu'

# Tarifas de ejemplo (puedes ajustarlas en el menú 3 después)
tarifas = {
    "75cl": {"Distribuidor": 10.20, "Horeca": 12.00, "Particular": 13.40},
    "25cl": {"Distribuidor": 5.00, "Horeca": 6.00, "Particular": 6.50}
}

# --- NAVEGACIÓN ---
if st.session_state.seccion == 'menu':
    st.image("Vermth de la aplicación/Logotipo-ideal-fruits.png", width=120)
    st.title("Panel de Gestión")
    
    if st.button("1. Gestionar Nuevo Pedido"):
        st.session_state.seccion = 'pedido'
        st.rerun()
    
    if st.button("2. Ver Stocks y Costes Actuales"):
        st.info("Sección en desarrollo")
        
    if st.button("3. Ajustar Stocks, Costes y Tarifas"):
        st.info("Sección en desarrollo")
        
    if st.button("4. Salir"):
        st.session_state.clear()
        st.rerun()

elif st.session_state.seccion == 'pedido':
    st.header("🛒 Nuevo Pedido")
    if st.button("⬅️ Volver"):
        st.session_state.seccion = 'menu'
        st.rerun()
    
    with st.form("form_pedido"):
        cliente = st.text_input("Cliente")
        formato = st.selectbox("Formato", ["75cl", "25cl"])
        tipo = st.selectbox("Tipo de Cliente", ["Distribuidor", "Horeca", "Particular"])
        cantidad = st.number_input("Cantidad de botellas", min_value=1, step=1)
        
        precio_sugerido = tarifas[formato][tipo]
        st.write(f"**Precio Tarifa:** {precio_sugerido}€")
        precio_final = st.number_input("Precio Final Unitario (€)", value=float(precio_sugerido))
        
        enviado = st.form_submit_button("Confirmar y Guardar")
        if enviado:
            total = precio_final * cantidad
            st.success(f"¡Venta registrada! Total: {total:.2f}€")
            time.sleep(2)
            st.session_state.seccion = 'menu'
            st.rerun()
