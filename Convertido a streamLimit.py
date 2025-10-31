import streamlit as st

# === ESTILOS PERSONALIZADOS (fondo rosita con emojis) ===
st.markdown(
    """
    <style>
    body {
        background-color: #ffe6f2;  /* Fondo rosita pastel */
        background-image: 
            radial-gradient(circle, transparent 20%, #ffe6f2 20%), 
            radial-gradient(circle, transparent 20%, #ffe6f2 20%), 
            radial-gradient(circle, transparent 20%, #ffe6f2 20%),
            radial-gradient(🌸 10px, transparent 12px),
            radial-gradient(💖 10px, transparent 12px),
            radial-gradient(✨ 10px, transparent 12px),
            radial-gradient(🌷 10px, transparent 12px);
        background-size: 120px 120px;
        background-position: 0 0, 60px 60px, 30px 90px, 90px 30px, 45px 45px;
    }

    h1 {
        color: #222;
        text-align: center;
        font-family: 'Poppins', sans-serif;
    }

    label, .stSelectbox label, .stNumberInput label, .stTextInput label {
        color: #222 !important;
        font-weight: 600;
    }

    .stButton>button {
        background-color: #ff4da6;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #ff80bf;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === TÍTULO ===
st.markdown("<h1>🌸 Calculadora 💖</h1>", unsafe_allow_html=True)

# === CATEGORÍAS ===
categorias = {
    "Longitud": {
        "milímetro": 0.001,
        "centímetro": 0.01,
        "metro": 1,
        "kilómetro": 1000,
        "pulgada": 0.0254,
        "pie": 0.3048,
        "yarda": 0.9144,
        "milla": 1609.34,
    },
    "Masa": {
        "miligramo": 0.001,
        "gramo": 1,
        "kilogramo": 1000,
        "tonelada": 1_000_000,
        "onza": 28.3495,
        "libra": 453.592,
        "tonelada corta": 907_185,
        "tonelada larga": 1_016_047,
    },
    "Velocidad": {
        "metro/segundo": 1,
        "kilómetro/hora": 0.277778,
        "milla/hora": 0.44704,
        "nudo": 0.514444,
        "pie/segundo": 0.3048,
    },
    "Aceleración": {
        "metro/segundo²": 1,
        "kilómetro/hora²": 0.00007716,
        "pie/segundo²": 0.3048,
        "gal (cm/s²)": 0.01,
        "g (gravedad terrestre)": 9.80665,
    },
    "Fuerza": {
        "newton": 1,
        "kilonewton": 1000,
        "libra-fuerza": 4.44822,
        "dina": 1e-5,
        "kilogramo-fuerza": 9.80665,
    },
    "Temperatura": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K",
    },
}

# === SELECCIÓN DE CATEGORÍA ===
categoria = st.selectbox("Selecciona una categoría:", list(categorias.keys()))

# === SELECCIÓN DE UNIDADES ===
if categoria == "Temperatura":
    origen = st.selectbox("Unidad de origen:", list(categorias[categoria].keys()))
    destino = st.selectbox("Unidad destino:", list(categorias[categoria].keys()))
    valor = st.number_input(f"Valor en {origen}:", step=0.01)

    def convertir_temp(valor, origen, destino):
        if origen == destino:
            return valor
        if origen == "Celsius":
            if destino == "Fahrenheit":
                return valor * 9 / 5 + 32
            elif destino == "Kelvin":
                return valor + 273.15
        elif origen == "Fahrenheit":
            if destino == "Celsius":
                return (valor - 32) * 5 / 9
            elif destino == "Kelvin":
                return (valor - 32) * 5 / 9 + 273.15
        elif origen == "Kelvin":
            if destino == "Celsius":
                return valor - 273.15
            elif destino == "Fahrenheit":
                return (valor - 273.15) * 9 / 5 + 32

    if st.button("Calcular"):
        resultado = convertir_temp(valor, origen, destino)
        st.success(f"🌷 {valor:.2f} {origen} equivalen a {resultado:.2f} {destino}")

else:
    unidades = categorias[categoria]
    origen = st.selectbox("Unidad de origen:", list(unidades.keys()))
    destino = st.selectbox("Unidad destino:", list(unidades.keys()))
    valor = st.number_input(f"Valor en {origen}:", step=0.01)

    if st.button("Calcular"):
        valor_base = valor * unidades[origen]
        resultado = valor_base / unidades[destino]
        st.success(f"🌸 {valor:.5f} {origen} equivalen a {resultado:.5f} {destino}")
