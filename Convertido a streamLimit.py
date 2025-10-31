import streamlit as st

# --- Configuración de la página ---
st.set_page_config(
    page_title="Calculadora",
    layout="centered"
)

# Fondo con la imagen de emojis 🎉
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/AlanYahir450/Calculadora-/main/7359978.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    h1, label, .stMarkdown, .stTextInput label, .stSelectbox label, .stNumberInput label {
        color: black !important;
        font-weight: bold;
    }
    .stButton button {
        background-color: #ff4081;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #e91e63;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Calculadora")

# --- Categorías de conversión ---
categorias = {
    "Longitud": {
        "milímetro": 0.001,
        "centímetro": 0.01,
        "metro": 1.0,
        "kilómetro": 1000.0,
        "pulgada": 0.0254,
        "pie": 0.3048,
        "yarda": 0.9144,
        "milla": 1609.34
    },
    "Masa": {
        "miligramo": 0.001,
        "gramo": 1.0,
        "kilogramo": 1000.0,
        "tonelada": 1_000_000.0,
        "onza": 28.3495,
        "libra": 453.592,
        "tonelada corta": 907_185.0,
        "tonelada larga": 1_016_046.9
    },
    "Velocidad y Aceleración": {
        "m/s": 1.0,
        "km/h": 0.277778,
        "mph": 0.44704,
        "nudo": 0.514444,
        "ft/s": 0.3048
    },
    "Fuerza": {
        "newton": 1.0,
        "kilonewton": 1000.0,
        "libra-fuerza": 4.44822,
        "dina": 1e-5,
        "kilogramo-fuerza": 9.80665
    },
    "Temperatura": None
}

# --- Interfaz de selección ---
categoria = st.selectbox("Selecciona una categoría:", list(categorias.keys()))

if categoria != "Temperatura":
    unidades = list(categorias[categoria].keys())
    origen = st.selectbox("Unidad de origen:", unidades)
    destino = st.selectbox("Unidad destino:", unidades)
    valor = st.number_input(f"Valor en {origen}:", min_value=0.0, format="%.6f")

    if st.button("Calcular"):
        if origen == destino:
            resultado = valor
        else:
            resultado = valor * categorias[categoria][origen] / categorias[categoria][destino]
        st.success(f"✅ {valor:.6f} {origen} equivalen a {resultado:.6f} {destino}")

else:
    origen = st.selectbox("Unidad de origen:", ["Celsius", "Fahrenheit", "Kelvin"])
    destino = st.selectbox("Unidad destino:", ["Celsius", "Fahrenheit", "Kelvin"])
    valor = st.number_input(f"Valor en {origen}:", format="%.2f")

    if st.button("Calcular"):
        resultado = None
        if origen == destino:
            resultado = valor
        elif origen == "Celsius" and destino == "Fahrenheit":
            resultado = (valor * 9/5) + 32
        elif origen == "Fahrenheit" and destino == "Celsius":
            resultado = (valor - 32) * 5/9
        elif origen == "Celsius" and destino == "Kelvin":
            resultado = valor + 273.15
        elif origen == "Kelvin" and destino == "Celsius":
            resultado = valor - 273.15
        elif origen == "Fahrenheit" and destino == "Kelvin":
            resultado = (valor - 32) * 5/9 + 273.15
        elif origen == "Kelvin" and destino == "Fahrenheit":
            resultado = (valor - 273.15) * 9/5 + 32

        if resultado is not None:
            st.success(f"✅ {valor:.2f} {origen} equivalen a {resultado:.2f} {destino}")
