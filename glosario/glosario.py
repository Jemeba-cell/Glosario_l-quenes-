import streamlit as st
from streamlit_carousel import carousel
import base64
from pathlib import Path

# Directorio donde está este script (glosario/) para que las rutas de imágenes funcionen siempre
SCRIPT_DIR = Path(__file__).resolve().parent

#PRUEBA DE SUBIR A GITHUB CAMBIOS


# --- Configuración de página (debe ir primero en Streamlit) ---
st.set_page_config(
    page_title="Glosario de Liquenología",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Cargar imagen en base64 ---
def get_image_base64(image_file):
    """Acepta ruta relativa a glosario/ o Path. Resuelve desde SCRIPT_DIR."""
    path = Path(image_file) if isinstance(image_file, str) else image_file
    if not path.is_absolute():
        path = SCRIPT_DIR / path
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None


def path_imagen(rel_path):
    """Convierte ruta relativa (ej. imagenes/fondo1.jpg) en path absoluto respecto al script."""
    return str(SCRIPT_DIR / rel_path)

# --- Estilos globales ---
def inject_custom_css():
    fondo_b64 = get_image_base64(path_imagen("imagenes/fondo1.jpg"))
    fondo_css = f'url("data:image/jpeg;base64,{fondo_b64}")' if fondo_b64 else "none"

    st.markdown(
        f"""
        <style>
        /* === Fondo y contenedor principal === */
        .stApp {{
            background-image: {fondo_css};
            background-color: #0a1f18;
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stApp::before {{
            content: "";
            position: fixed;
            inset: 0;
            background: linear-gradient(180deg, rgba(0,30,20,0.85) 0%, rgba(0,20,15,0.9) 100%);
            pointer-events: none;
            z-index: 0;
        }}
        .block-container {{
            padding: 2rem 3rem 3rem;
            max-width: 1100px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }}

        /* === Título === */
        h1 {{
            font-family: Georgia, 'Times New Roman', serif !important;
            font-weight: 700 !important;
            font-size: 2.2rem !important;
            color: #f0f8f0 !important;
            text-align: center;
            margin-bottom: 0.25rem !important;
            text-shadow: 0 2px 12px rgba(0,0,0,0.5);
        }}
        .subtitle {{
            text-align: center;
            color: rgba(240,248,240,0.85) !important;
            font-size: 1rem;
            margin-bottom: 2rem;
        }}

        /* === Buscador === */
        .stTextInput > div > div > input {{
            background: rgba(255,255,255,0.12) !important;
            border: 1px solid rgba(255,255,255,0.25) !important;
            border-radius: 12px !important;
            color: #f0f8f0 !important;
            padding: 0.75rem 1rem !important;
            font-size: 1rem !important;
        }}
        .stTextInput > div > div > input::placeholder {{
            color: rgba(240,248,240,0.6) !important;
        }}
        .stTextInput > div > div > input:focus {{
            border-color: rgba(144,238,144,0.6) !important;
            box-shadow: 0 0 0 2px rgba(144,238,144,0.2) !important;
        }}

        /* === Tarjeta de resultado del glosario === */
        .glosario-card-anchor + div {{
            background: rgba(0,40,30,0.75) !important;
            border: 1px solid rgba(144,238,144,0.25) !important;
            border-radius: 16px !important;
            padding: 1.5rem 2rem !important;
            margin: 1rem 0 !important;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
        }}
        .glosario-card-anchor + div h3 {{
            color: #b8e6b8 !important;
            font-size: 1.5rem !important;
            margin-bottom: 0.75rem !important;
        }}
        .glosario-card-anchor + div p {{
            color: rgba(240,248,240,0.95) !important;
            line-height: 1.6;
        }}

        /* === Texto general === */
        .stMarkdown, .stMarkdown p, [data-testid="stMarkdownContainer"] {{
            color: rgba(240,248,240,0.9) !important;
        }}
        hr {{
            margin: 2rem 0 !important;
            border: none !important;
            height: 1px !important;
            background: linear-gradient(90deg, transparent, rgba(144,238,144,0.35), transparent) !important;
        }}

        /* === Sección carrusel === */
        .section-title {{
            color: #b8e6b8 !important;
            font-size: 1.25rem !important;
            margin-bottom: 1rem !important;
        }}
        /* Contenedor del iframe del carrusel */
        div:has(iframe[title="streamlit_carousel.streamlit_carousel"]) {{
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 12px 40px rgba(0,0,0,0.4);
            margin: 0 auto 1rem;
            max-width: 900px;
        }}
        div:has(iframe[title="streamlit_carousel.streamlit_carousel"]) iframe {{
            width: 100% !important;
            height: 420px !important;
            max-width: 900px !important;
            border: none !important;
        }}

        /* === Sidebar (expandido y colapsado) === */
        [data-testid="stSidebar"],
        [data-testid="stSidebar"][aria-expanded="true"],
        [data-testid="stSidebar"] > div {{
            background: #f4faf4 !important;
        }}
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] .stMarkdown p,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span:not([class*="Icon"]) {{
            color: #1a2e1a !important;
        }}
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {{
            color: #0d3d2d !important;
        }}
        [data-testid="stSidebar"] .stRadio label {{
            font-size: 0.9rem !important;
            color: #1a2e1a !important;
        }}
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {{
            color: #1a2e1a !important;
        }}
        [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
            color: #2d4a2d !important;
        }}
        .sidebar-selected {{
            background: rgba(0,80,60,0.15) !important;
            padding: 0.5rem 0.75rem;
            border-radius: 8px;
            font-weight: 600;
            color: #0d3d2d !important;
        }}
        /* Evitar que el tema claro de Streamlit sobrescriba en el sidebar */
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
            color: inherit;
        }}

        /* === Aviso "término no encontrado" === */
        [data-testid="stAlert"] {{
            background: rgba(0,40,30,0.85) !important;
            border: 1px solid rgba(255,180,100,0.4) !important;
            border-radius: 12px !important;
            color: #f0f8f0 !important;
        }}

        /* === Caption / pie de texto en main === */
        .main .stCaption {{
            color: rgba(240,248,240,0.75) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

inject_custom_css()

# --- Cabecera ---
st.title("🌿 Glosario Interactivo de Liquenología")
st.markdown(
    '<p class="subtitle">Busca términos, explora el carrusel y navega por categorías</p>',
    unsafe_allow_html=True,
)

# --- Glosario ---
glosario = {
    "Soredio": {"descripcion": "Estructura de dispersión...", "imagen": path_imagen("imagenes/soredio.jpeg")},
    "Soralio": {"descripcion": "Área del talo...", "imagen": path_imagen("imagenes/soralio.jpeg")},
    "Isidio": {"descripcion": "Pequeñas prolongaciones...", "imagen": path_imagen("imagenes/isidios.jpeg")},
    "Apotecio": {"descripcion": "Estructura reproductora sexual...", "imagen": path_imagen("imagenes/apotecio.jpg")},
    "Picnidio": {"descripcion": "Estructura reproductora asexual...", "imagen": path_imagen("imagenes/picnidio.jfif")},
    "Folioso": {"descripcion": "Líquenes con lóbulos planos...", "imagen": path_imagen("imagenes/folioso.jpg")},
    "Fruticoso": {"descripcion": "Líquenes ramificados...", "imagen": path_imagen("imagenes/fruticoso.jpg")},
    "Costroso": {"descripcion": "Líquenes adheridos al sustrato...", "imagen": path_imagen("imagenes/costroso.jfif")},
    "Gelatinoso": {"descripcion": "Talo flexible y gelatinoso...", "imagen": path_imagen("imagenes/gelatinoso.jfif")},
    "Compuesto": {"descripcion": "Combinación de formas...", "imagen": path_imagen("imagenes/compuesto.jfif")},
}

termino = st.text_input("", placeholder="🔍 Escribe un término del glosario", label_visibility="collapsed")
if termino:
    termino_cap = termino.strip().capitalize()
    if termino_cap in glosario:
        info = glosario[termino_cap]
        st.markdown('<div class="glosario-card-anchor" aria-hidden="true"></div>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(info["imagen"], use_container_width=True)
        with col2:
            st.markdown(f"### {termino_cap}")
            st.write(info["descripcion"])
    else:
        st.warning("Ese término no está en el glosario.")

st.markdown("---")

# --- Acerca del proyecto + Carrusel ---
st.markdown('<p class="section-title">Acerca del proyecto</p>', unsafe_allow_html=True)

imagenes_carrusel = [
    {"img": path_imagen("imagenes/Carrusel1.png"), "title": "", "text": ""},
    {"img": path_imagen("imagenes/Carrusel2.jpg"), "title": "", "text": ""},
    {"img": path_imagen("imagenes/Carrusel3.jpg"), "title": "", "text": ""},
    {"img": path_imagen("imagenes/Carrusel4.jpg"), "title": "", "text": ""},
]
carousel(items=imagenes_carrusel, container_height=420)

st.markdown("---")

# --- Sidebar: categorías ---
categorias = [
    "Anatomía y Morfología",
    "Ecología",
    "Evolución",
    "Biogeografía",
    "Historia",
    "Metabolitos secundarios",
    "Metabolismo y Nutrición",
    "Morfogénesis del Talo",
    "Reproducción",
    "Sistemática y Taxonomía",
]

st.sidebar.markdown("### 📚 Categorías")
cat = st.sidebar.radio("Elige una categoría:", categorias, label_visibility="collapsed")
st.sidebar.markdown(
    f'<p class="sidebar-selected">Has seleccionado: {cat}</p>',
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")
st.sidebar.caption(
    "Los conceptos específicos (apotecio, soralio, isidios, etc.) están disponibles en el buscador principal."
)
