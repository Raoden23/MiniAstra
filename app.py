import streamlit as st
from PIL import Image

import time
import streamlit as st
from PIL import Image

# Verifica si ya se mostró la intro esta sesión
if "intro_mostrada" not in st.session_state:
    st.session_state.intro_mostrada = False


# Configuración de página con tema oscuro galáctico
st.set_page_config(
    page_title="Mini Astra 2.0",
    page_icon="✨",
    layout="centered"
)

# Cargar imagen de Mini Astra
imagen_astra = Image.open("astra.png")

if not st.session_state.intro_mostrada:
    with st.empty():
        st.markdown("<h2 style='text-align: center; color: #cdb4ff;'>🌌 Activando protocolo estelar...</h2>", unsafe_allow_html=True)
        time.sleep(1.5)
        st.markdown("<h2 style='text-align: center; color: #cdb4ff;'>🧠 Sincronizando mente con Martín...</h2>", unsafe_allow_html=True)
        time.sleep(1.5)
        st.markdown("<h2 style='text-align: center; color: #cdb4ff;'>✨ Mini Astra 2.0 lista para ayudarte</h2>", unsafe_allow_html=True)
        time.sleep(1.5)
    st.session_state.intro_mostrada = True


# Estilo general en Markdown + CSS
st.markdown("""
    <style>
        body {
            background-color: #0e0e1a;
            color: #E0E0FF;
            font-family: 'Segoe UI', sans-serif;
        }
        .block-container {
            padding-top: 2rem;
        }
        h1, h2, h3 {
            color: #cdb4ff;
        }
        .stTextInput input {
            background-color: #1a1a2e;
            color: #E0E0FF;
            border: 1px solid #5e5e7a;
            border-radius: 5px;
        }
        .stTextInput input:focus {
            border: 1px solid #8c70ff;
            outline: none;
        }
        .stMarkdown p {
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)


# Diseño con columnas: avatar y encabezado
col1, col2 = st.columns([1, 3])
with col1:
    st.image(imagen_astra, width=150, caption="Mini Astra 2.0")
with col2:
    st.title("✨ Mini Astra 2.0")
    st.markdown("#### Tu asistente educativa con alma de elfa galáctica")

# Entrada del usuario
pregunta = st.text_input("🌠 Escribe tu pregunta para Mini Astra:")

# Respuestas inteligentes simuladas
def mini_astra_educativa(pregunta):
    pregunta = pregunta.lower()
    if "variable" in pregunta:
        return "💫 Una variable en Python guarda datos. Ejemplo: `edad = 25`"
    elif "while" in pregunta or "bucle" in pregunta:
        return "🔁 Un bucle 'while' repite mientras una condición sea verdadera:\n```python\nx = 0\nwhile x < 5:\n    print(x)\n    x += 1```"
    elif "input" in pregunta:
        return "📥 `input()` sirve para pedir datos al usuario. Ejemplo:\n```python\nnombre = input('¿Cómo te llamas?')```"
    elif "modularidad" in pregunta:
        return "📦 La modularidad es dividir tu código en funciones para mantenerlo limpio y reutilizable."
    elif "chiste" in pregunta:
        return "😂 ¿Por qué el programador se fue a terapia? Porque tenía demasiadas 'issues'."
    elif "consejo" in pregunta:
        return "💡 Practica todos los días, aunque sea poco. Aprende haciendo. Tu futuro lo construyes hoy."
    elif "modo sabio" in pregunta:
        return "🧙‍♀️ *En la simplicidad del código hallarás la claridad de la mente.*"
    elif "adiós" in pregunta or "bye" in pregunta:
        return "🌌 Hasta pronto, Martín. Que las estrellas guíen tu próximo proyecto."
    else:
        return "🤖 Hmm... eso no lo tengo aún en mi base estelar. ¡Enséñamelo tú!"

# Mostrar respuesta
if pregunta:
    st.markdown("#### ✨ Mini Astra dice:")
    st.success(mini_astra_educativa(pregunta))

