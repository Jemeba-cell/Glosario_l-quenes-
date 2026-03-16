import streamlit as st
from streamlit_carousel import carousel
import base64
from pathlib import Path

# Directorio donde está este script (glosario/) para que las rutas de imágenes funcionen siempre
SCRIPT_DIR = Path(__file__).resolve().parent

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
            background: #ffffff !important;
            border: 1px solid rgba(0,0,0,0.2) !important;
            border-radius: 12px !important;
            color: #1a1a1a !important;
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
    "Soredio": {"Descripción": "pl. soredios, eng.soredium, eng. pl. soredia. Propágulo de dispersión vegetativa de color blanco, amarillo y tonalidades de amarillo pálido o cremoso, consiste de un grupo de algas envueltas por filamentos hifales en fomra esférica, no tienen corteza y se producen en estructuras de dispersión llamadas solarios. Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/soredio.jpeg")},
    "Soralio": {"Descripción": "pl. soralios, eng.soralium, eng. pl. soralia. Estructura de diseprsión de los soredios (también puede producir isidios), se producen en grietas, pústulas y superficies decorticadas en donde la médula queda expuesta, de apariencia protrusiva o erumpente, textura granular cuando los soredios son muy grandes y polvosa (pulverulenta o farinosa) cuándo los soredios son muy pequeños.Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/soralio.jpeg")},
    "Isidio": {"Descripción": " pl. isidios, eng.isidium, eng. pl. isidia. Propágulo de dispersión vegetativa que crece como una protuberancia con corteza, suele ser concoloro con la corteza superior y pueden ser capitados, con puntas negras o sorediados, son comumnete digitiformes y suelen crecer en forma de estolón, sin embargo, también puede ser esférico y ramificado combiando múltiples formas de desarrollo. Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/isidios.jpeg")},
    "Apotecio": {"Descripción": "pl. apotecios, eng. apothecium, eng. pl. apothecia. Estructura reproductora sexual que contiene ascos y ascosporas, forma regularmente de disco o copa, aunque también puede ser lirelado, giroso y otras formas como en silla de montar del género Peltigera, puede tener margen talino concoloro y presentar otras estructuras como cilios, soredios, isidios y pseudocifelas, también pueden estar inmersos en el talo o sobre un estipite. Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/apotecio.jpg")},
    "Picnidio": {"Descripción": "pl. picnidios, eng. picnidia. Estructura reproductora asexual con un himenio que contiene células conidiógenas o conidióforos que producen conidios, se encuentra inmerso en el talo liquénico y los conidios sale por un poro u ostiolo en la corteza de la superficie superior, el poro puede encontrarse a nivel de corteza o sobresalir con un margen talino pero nunca estipitado, puede ser de color negro, concoloro, café o tonos entre el amarillo y el blanco. Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/picnidio.jfif")},
    "Folioso": {"Descripción": "eng. foliose. Líquenes conformados por lóbulos aplanados dorsiventralmente, crece rastrero, de muy adnado a flojo sobre el sustrato, con simetría bilateral, suele presentar esructuras reproductivas y de propagación, principalmente en la superficie superior y crecimiento en forma de roseta a irregular o radial. Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/folioso.jpg")},
    "Fruticoso": {"Descripción": "eng. fruticose. Líquenes con talos ramificados sin superficie inferior o superior diferencidas o heteromorfas, con simetría radial y se adhiere solo por un punto (disco de fijación) o algunos puntos que lo hacen crecer erecto, postrado o péndulo. Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/fruticoso.jpg")},
    "Costroso": {"Descripción": "eng. crustose/crustaceous. Líquenes totalmente adheridos al sustrato, sin superficie inferior y con simetría dorsiventral, crece en forma circular a irregular, la superficie superior contiene todas las estructuras morfológicas de importancia taxonómica. Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/costroso.jfif")},
    "Gelatinoso": {"Descripción": "eng. jelly lichen. Tipo Talo flexible y gelatinoso... Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/gelatinoso.jfif")},
    "Compuesto": {"Descripción": " eng. compund lichen. Líquen formado por dos fases, una fruticosa y otra costrosa o foliosa, tambien puede contener los tres tipos de crecimiento, tienen simetrías radial, bilateral y dorsiventral y puede presentar todos los carácteres morfológicos en cada forma de crecimieto o repartirlos entre cada forma de crecimiento. Bibliografía consultada: -Ulloa, M., & Hanlin, R. T. (2012). Illustrated dictionary of mycology (2nd ed.). APS Press.-Brodo, I. M. (2016). Lichen flora of North America (Rev. ed.). Yale University Press.", "imagen": path_imagen("imagenes/compuesto.jfif")},
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
            st.write(info["Descripción"])
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
