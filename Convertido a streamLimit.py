import streamlit as st

# --- CONFIGURACIÓN DE LA APP ---
st.set_page_config(page_title="Calculadora", page_icon="💖", layout="centered")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
        color: #4a4a4a;
        font-family: 'Poppins', sans-serif;
    }
    .stApp {
        background-color: #ffe6f0;
    }
    h1 {
        text-align: center;
        color: #ff4da6;
        font-weight: 700;
        font-size: 42px;
    }
    .stSelectbox, .stTextInput, .stButton>button {
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #ff4da6;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff66b2;
    }
    </style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.title("Calculadora")

# --- MENÚ PRINCIPAL ---
categoria = st.selectbox("Selecciona una categoría:", [
    "Longitud",
    "Masa",
    "Velocidad y Aceleración",
    "Fuerza",
    "Temperatura"
])

# --- LONGITUD ---
if categoria == "Longitud":
    unidades = {
        "milímetro": 0.001,
        "centímetro": 0.01,
        "metro": 1,
        "kilómetro": 1000,
        "pulgada": 0.0254,
        "pie": 0.3048,
        "yarda": 0.9144,
        "milla": 1609.34
    }

    origen = st.selectbox("Unidad de origen:", unidades.keys())
    destino = st.selectbox("Unidad destino:", unidades.keys())
    valor = st.number_input(f"Valor en {origen}:", min_value=0.0, format="%.5f")

    if st.button("Calcular"):
        resultado = valor * unidades[origen] / unidades[destino]
        st.success(f"✅ {valor:.5f} {origen} equivalen a {resultado:.5f} {destino}")

# --- MASA ---
elif categoria == "Masa":
    unidades = {
        "miligramo": 0.001,
        "gramo": 1,
        "kilogramo": 1000,
        "tonelada": 1_000_000,
        "onza": 28.3495,
        "libra": 453.592,
        "tonelada corta": 907_185,
        "tonelada larga": 1_016_047
    }

    origen = st.selectbox("Unidad de origen:", unidades.keys())
    destino = st.selectbox("Unidad destino:", unidades.keys())
    valor = st.number_input(f"Valor en {origen}:", min_value=0.0, format="%.5f")

    if st.button("Calcular"):
        resultado = valor * unidades[origen] / unidades[destino]
        st.success(f"✅ {valor:.5f} {origen} equivalen a {resultado:.5f} {destino}")

# --- VELOCIDAD Y ACELERACIÓN ---
elif categoria == "Velocidad y Aceleración":
    tipo = st.radio("¿Qué deseas convertir?", ["Velocidad", "Aceleración"])

    if tipo == "Velocidad":
        unidades = {
            "metro/segundo": 1,
            "kilómetro/hora": 0.277778,
            "milla/hora": 0.44704,
            "nudo": 0.514444,
            "pie/segundo": 0.3048
        }
    else:
        unidades = {
            "metro/segundo²": 1,
            "kilómetro/hora²": 0.00007716,
            "pie/segundo²": 0.3048,
            "gal (cm/s²)": 0.01,
            "g (gravedad terrestre)": 9.80665
        }

    origen = st.selectbox("Unidad de origen:", unidades.keys())
    destino = st.selectbox("Unidad destino:", unidades.keys())
    valor = st.number_input(f"Valor en {origen}:", min_value=0.0, format="%.5f")

    if st.button("Calcular"):
        resultado = valor * unidades[origen] / unidades[destino]
        st.success(f"✅ {valor:.5f} {origen} equivalen a {resultado:.5f} {destino}")

# --- FUERZA ---
elif categoria == "Fuerza":
    unidades = {
        "newton": 1,
        "kilonewton": 1000,
        "libra-fuerza": 4.44822,
        "dina": 0.00001,
        "kilogramo-fuerza": 9.80665
    }

    origen = st.selectbox("Unidad de origen:", unidades.keys())
    destino = st.selectbox("Unidad destino:", unidades.keys())
    valor = st.number_input(f"Valor en {origen}:", min_value=0.0, format="%.5f")

    if st.button("Calcular"):
        resultado = valor * unidades[origen] / unidades[destino]
        st.success(f"✅ {valor:.5f} {origen} equivalen a {resultado:.5f} {destino}")

# --- TEMPERATURA ---
elif categoria == "Temperatura":
    origen = st.selectbox("Unidad de origen:", ["Celsius", "Fahrenheit", "Kelvin"])
    destino = st.selectbox("Unidad destino:", ["Celsius", "Fahrenheit", "Kelvin"])
    valor = st.number_input(f"Valor en {origen}:", format="%.2f")

    if st.button("Calcular"):
        temp = valor
        if origen == "Celsius":
            if destino == "Fahrenheit":
                temp = valor * 9 / 5 + 32
            elif destino == "Kelvin":
                temp = valor + 273.15
        elif origen == "Fahrenheit":
            if destino == "Celsius":
                temp = (valor - 32) * 5 / 9
            elif destino == "Kelvin":
                temp = (valor - 32) * 5 / 9 + 273.15
        elif origen == "Kelvin":
            if destino == "Celsius":
                temp = valor - 273.15
            elif destino == "Fahrenheit":
                temp = (valor - 273.15) * 9 / 5 + 32

        st.success(f"🌸 {valor:.2f} {origen} equivalen a {temp:.2f} {destino}")
