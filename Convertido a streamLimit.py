import streamlit as st

# Configuración de página
st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

# === Estilos con fondo ===
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: url("7359978.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.block-container {
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 20px;
    padding: 30px;
    margin-top: 50px;
    box-shadow: 0 0 25px rgba(0,0,0,0.15);
}

h1 {
    color: #ff4081;
    text-align: center;
    font-weight: 900;
}

label, p, div, span {
    color: #000000 !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# === Título ===
st.markdown("<h1>Calculadora</h1>", unsafe_allow_html=True)

# === Categorías ===
categorias = {
    "Longitud": {
        "milímetro": 0.001,
        "centímetro": 0.01,
        "metro": 1,
        "kilómetro": 1000,
        "pulgada": 0.0254,
        "pie": 0.3048,
        "yarda": 0.9144,
        "milla": 1609.34
    },
    "Masa": {
        "miligramo": 0.001,
        "gramo": 1,
        "kilogramo": 1000,
        "tonelada": 1000000,
        "onza": 28.3495,
        "libra": 453.592
    },
    "Velocidad y Aceleración": {
        "metro/segundo": 1,
        "kilómetro/hora": 0.277778,
        "milla/hora": 0.44704,
        "nudo": 0.514444,
        "pie/segundo": 0.3048
    },
    "Fuerza": {
        "newton": 1,
        "kilonewton": 1000,
        "libra-fuerza": 4.44822,
        "dina": 0.00001,
        "kilogramo-fuerza": 9.80665
    },
    "Temperatura": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}

# === Selección de categoría ===
categoria = st.selectbox("Selecciona una categoría:", list(categorias.keys()))

# === Lógica de conversión ===
if categoria == "Temperatura":
    unidades = list(categorias[categoria].keys())
    origen = st.selectbox("Unidad de origen:", unidades)
    destino = st.selectbox("Unidad destino:", unidades)
    valor = st.number_input(f"Valor en {origen.lower()}:", format="%.2f", step=0.1)

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
            st.success(f"🌡️ {valor} {origen} equivalen a {resultado:.2f} {destino}")

else:
    unidades = list(categorias[categoria].keys())
    origen = st.selectbox("Unidad de origen:", unidades)
    destino = st.selectbox("Unidad destino:", unidades)
    valor = st.number_input(f"Valor en {origen.lower()}:", format="%.5f", step=0.1)

    if st.button("Calcular"):
        try:
            valor_base = valor * categorias[categoria][origen]
            resultado = valor_base / categorias[categoria][destino]
            st.success(f"✅ {valor:.5f} {origen} equivalen a {resultado:.5f} {destino}")
        except Exception as e:
            st.error("Error en la conversión. Verifica las unidades seleccionadas.")
