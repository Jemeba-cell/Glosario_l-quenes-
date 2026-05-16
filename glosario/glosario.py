import streamlit as st
from pathlib import Path
import base64

SCRIPT_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Glosario de Liquenología",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# UTILIDADES DE IMAGEN
# ─────────────────────────────────────────────
def get_image_base64(image_file):
    path = Path(image_file) if isinstance(image_file, str) else image_file
    if not path.is_absolute():
        path = SCRIPT_DIR / path
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except (FileNotFoundError, OSError):
        return None

def path_imagen(rel_path):
    return str(SCRIPT_DIR / rel_path)

# ─────────────────────────────────────────────
# DATOS: glosario principal
# ─────────────────────────────────────────────
glosario = {
    "Soredio": {
        "Descripción": "pl. soredios, eng. soredium, eng. pl. soredia. Propágulo de dispersión vegetativa de color blanco, amarillo y tonalidades de amarillo pálido o cremoso, consiste de un grupo de algas envueltas por filamentos hifales en forma esférica, no tienen corteza y se producen en estructuras de dispersión llamadas soralios. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/soredio.jpeg"),
    },
    "Soralio": {
        "Descripción": "pl. soralios, eng. soralium, eng. pl. soralia. Estructura de dispersión de los soredios, se producen en grietas, pústulas y superficies decorticadas en donde la médula queda expuesta, de apariencia protrusiva o erumpente, textura granular o pulverulenta. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/soralio.jpeg"),
    },
    "Isidio": {
        "Descripción": "pl. isidios, eng. isidium, eng. pl. isidia. Propágulo de dispersión vegetativa que crece como una protuberancia con corteza, suele ser concoloro con la corteza superior, comúnmente digitiforme, puede ser esférico y ramificado. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/isidios.jpeg"),
    },
    "Apotecio": {
        "Descripción": "pl. apotecios, eng. apothecium, eng. pl. apothecia. Estructura reproductora sexual que contiene ascos y ascosporas, forma regularmente de disco o copa, puede tener margen talino y presentar otras estructuras como cilios, soredios o isidios. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/apotecio.jpg"),
    },
    "Picnidio": {
        "Descripción": "pl. picnidios, eng. pycnidia. Estructura reproductora asexual con un himenio que produce conidios, se encuentra inmerso en el talo liquénico y los conidios salen por un poro u ostiolo. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/picnidio.jfif"),
    },
    "Folioso": {
        "Descripción": "eng. foliose. Líquenes conformados por lóbulos aplanados dorsiventralmente, crece rastrero sobre el sustrato, con simetría bilateral, suele presentar estructuras reproductivas principalmente en la superficie superior. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/folioso.jpg"),
    },
    "Fruticoso": {
        "Descripción": "eng. fruticose. Líquenes con talos ramificados sin superficie inferior o superior diferenciadas, con simetría radial y se adhiere solo por un punto, puede crecer erecto, postrado o péndulo. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/fruticoso.jpg"),
    },
    "Costroso": {
        "Descripción": "eng. crustose/crustaceous. Líquenes totalmente adheridos al sustrato, sin superficie inferior y con simetría dorsiventral, crece en forma circular a irregular. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/costroso.jfif"),
    },
    "Gelatinoso": {
        "Descripción": "eng. jelly lichen. Tipo de talo flexible y gelatinoso. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/gelatinoso.jfif"),
    },
    "Compuesto": {
        "Descripción": "eng. compound lichen. Líquen formado por dos fases, una fruticosa y otra costrosa o foliosa, también puede contener los tres tipos de crecimiento. Bibliografía: Ulloa & Hanlin (2012); Brodo (2016).",
        "imagen": path_imagen("imagenes/compuesto.jfif"),
    },
}

# ─────────────────────────────────────────────
# DATOS: DEFINICIONES POST-IT (Definición Ecológica)
# ─────────────────────────────────────────────
DEFINICIONES_POSTIT = {
    "asociación simbiótica mutualista": {
        "titulo": "Asociación Simbiótica Mutualista",
        "definicion": "Relación biológica íntima y duradera entre dos organismos de especies diferentes (hongo + alga/cianobacteria) donde ambos se benefician: el hongo proporciona estructura, protección y nutrientes, mientras el fotobionte aporta carbohidratos mediante fotosíntesis. Es la base de la organización del talo liquénico."
    },
    "ecológicamente estable": {
        "titulo": "Ecológicamente Estable",
        "definicion": "Condición de un sistema o asociación que mantiene sus propiedades estructurales y funcionales a lo largo del tiempo frente a perturbaciones ambientales normales. En líquenes, implica la persistencia de la simbiosis sin desintegración del talo bajo condiciones ambientales variables."
    },
    "umbrales de resiliencia": {
        "titulo": "Umbrales de Resiliencia",
        "definicion": "Límites críticos de perturbación ambiental (humedad, temperatura, radiación, contaminantes) que un ecosistema o organismo puede tolerar antes de sufrir un cambio cualitativo irreversible. Los líquenes poseen umbrales amplios gracias a su poiquilohidria y metabolismo flexible."
    },
    "niveles tróficos": {
        "titulo": "Niveles Tróficos",
        "definicion": "Posiciones que ocupan los organismos en una cadena alimentaria según su fuente de energía y nutrientes. En líquenes, el fotobionte ocupa el nivel productor (autótrofo), mientras el micobionte es heterótrofo; juntos conforman una unidad funcional que interactúa con otros niveles del ecosistema."
    },
    "asociaciones dinámicas": {
        "titulo": "Asociaciones Dinámicas",
        "definicion": "Interacciones biológicas que cambian en intensidad, especificidad o composición a lo largo del tiempo o según condiciones ambientales. Los líquenes presentan asociaciones dinámicas porque pueden modificar la proporción hongo-alga, incorporar nuevos simbiontes o ajustar su fisiología según el hábitat."
    },
    "holobionte complejo": {
        "titulo": "Holobionte Complejo",
        "definicion": "Entidad biológica que funciona como un solo organismo pero está compuesta por el hospedero (hongo liquénico) y toda su microbiota asociada (algas, cianobacterias, bacterias, líquenes endofíticos y otros microorganismos), interactuando como una unidad de selección ecológica y evolutiva."
    }
}

# ─────────────────────────────────────────────
# DATOS: categorías y subtemas
# ─────────────────────────────────────────────
CATEGORIAS = {
    "🔬 Anatomía y Morfología": {
        "descripcion_general": "Estudio de la forma externa e interna de los líquenes.",
        "subtemas": {
            "Morfología externa": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Definición del talo liquénico": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Tipos de talo": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Estructuras reproductivas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🌱 Ecología": {
        "descripcion_general": "Estudio de las relaciones de los líquenes con el ambiente y otros organismos.",
        "subtemas": {
            "Introducción y bases ecológicas de los líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Definición ecológica de los líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Hipótesis 'Everything is everywhere, but the environment selects'": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Adaptaciones ecológicas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Roles ecológicos de los líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Indicadoras ambientales": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🧬 Evolución": {
        "descripcion_general": "Origen y diversificación de la simbiosis liquénica.",
        "subtemas": {
            "Origen evolutivo de la liquenización": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Definición evolutiva del líquen": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Coespeciación y cospeciación": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🗺️ Biogeografía": {
        "descripcion_general": "Patrones de distribución geográfica de los líquenes.",
        "subtemas": {
            "Distribución según la región": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "El Mar de Tetis": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "📜 Historia": {
        "descripcion_general": "Historia de la liquenología desde la antigüedad hasta la actualidad.",
        "subtemas": {
            "Los líquenes antes de Cristo": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Erick Acharius el padre de la liquenología": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Estudios de la liquenología en la actualidad": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "⚗️ Metabolitos Secundarios": {
        "descripcion_general": "Compuestos químicos únicos producidos por la simbiosis liquénica.",
        "subtemas": {
            "Origen de los metabolitos secundarios": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Rutas biosintéticas principales": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Detección de metabolitos": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🍃 Metabolismo y Nutrición": {
        "descripcion_general": "Procesos de intercambio de agua, carbono, nitrógeno y minerales.",
        "subtemas": {
            "Fotosíntesis y respiración": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Importancia del nitrógeno": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Metabolismo del nitrógeno": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🌀 Morfogénesis del Talo": {
        "descripcion_general": "Desarrollo y diferenciación de la estructura del líquen.",
        "subtemas": {
            "Particularidades de la simbiosis liquénica": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Reconocimiento y especificidad": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Diferenciación del talo estratificado": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🔁 Reproducción": {
        "descripcion_general": "Estrategias sexuales y asexuales de reproducción liquénica.",
        "subtemas": {
            "Reproducción sexual": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Diversidad de estructuras reproductivas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Morfogénesis de los soredios": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🏷️ Sistemática y Taxonomía": {
        "descripcion_general": "Organización de la diversidad liquénica en un sistema clasificatorio.",
        "subtemas": {
            "Conceptos clave en sistemática": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Principales órdenes y familias": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Géneros más representativos en México": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
}

# ─────────────────────────────────────────────
# CSS GLOBAL + POST-ITS
# ─────────────────────────────────────────────
def inject_css():
    fondo_b64 = get_image_base64(path_imagen("imagenes/fondo1.jpg"))
    fondo_css = f'url("data:image/jpeg;base64,{fondo_b64}")' if fondo_b64 else "none"

    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Source+Sans+3:wght@300;400;600&family=Patrick+Hand&display=swap');

    .stApp {{
        background-image: {fondo_css};
        background-color: #0a1f18;
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Source Sans 3', sans-serif;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: linear-gradient(180deg, rgba(0,30,20,0.85) 0%, rgba(0,20,15,0.92) 100%);
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
    h1 {{
        font-family: 'Lora', Georgia, serif !important;
        font-weight: 600 !important;
        font-size: 2.1rem !important;
        color: #d4edda !important;
        margin-bottom: 0.25rem !important;
        text-shadow: 0 2px 12px rgba(0,0,0,0.5);
    }}
    h2 {{
        font-family: 'Lora', Georgia, serif !important;
        color: #b8dfc0 !important;
        font-size: 1.45rem !important;
    }}
    h3 {{
        font-family: 'Lora', Georgia, serif !important;
        color: #9dd4aa !important;
        font-size: 1.15rem !important;
    }}
    .stMarkdown p, [data-testid="stMarkdownContainer"] p {{
        color:  #ffffff !important;
        font-family: 'Source Sans 3', sans-serif;
        line-height: 1.7;
         font-size: 1.5rem !important;
    }}
    .page-subtitle {{
        text-align: center;
        color: rgba(180,220,190,0.8) !important;
        font-size: 0.97rem;
        margin-bottom: 1.5rem;
        font-style: italic;
    }}
    .desc-general {{
        background: rgba(10,50,35,0.6);
        border: 1px solid rgba(100,180,130,0.2);
        border-left: 3px solid rgba(100,200,140,0.5);
        border-radius: 12px;
        padding: 1.5rem 2rem;
        color: rgba(220,240,225,0.92) !important;
        font-size: 1.02rem;
        line-height: 1.75;
        margin-bottom: 1.5rem;
    }}
    .subtema-card {{
        background: rgba(10,45,30,0.7);
        border: 1px solid rgba(100,180,130,0.25);
        border-radius: 16px;
        padding: 2rem;
        margin-top: 0.5rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }}
    .placeholder-badge {{
        display: inline-block;
        background: rgba(255,180,80,0.15);
        border: 1px solid rgba(255,180,80,0.35);
        color: rgba(255,200,120,0.9) !important;
        border-radius: 20px;
        padding: 0.2rem 0.75rem;
        font-size: 0.8rem;
        margin-bottom: 1rem;
    }}
    .stTextInput > div > div > input {{
        background: #ffffff !important;
        border: 1px solid rgba(0,0,0,0.2) !important;
        border-radius: 12px !important;
        color: #1a1a1a !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
    }}
    .stTextInput > div > div > input:focus {{
        border-color: rgba(144,238,144,0.6) !important;
        box-shadow: 0 0 0 2px rgba(144,238,144,0.2) !important;
    }}
    .glosario-result {{
        background: rgba(0,40,30,0.75);
        border: 1px solid rgba(144,238,144,0.25);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }}
    hr {{
        margin: 1.5rem 0 !important;
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg, transparent, rgba(100,180,130,0.35), transparent) !important;
    }}
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div {{
        background: #f0f7f2 !important;
    }}
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span:not([class*="Icon"]) {{
        color: #1a3025 !important;
    }}
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
        color: #0d3d2d !important;
    }}
    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
        color: #2d4a3a !important;
    }}
    [data-testid="stSidebar"] .stButton > button {{
        background: transparent !important;
        border: none !important;
        color: #1a3025 !important;
        text-align: left !important;
        font-size: 0.88rem !important;
        padding: 0.3rem 0.5rem !important;
        border-radius: 6px !important;
    }}
    [data-testid="stSidebar"] .stButton > button:hover {{
        background: rgba(0,80,50,0.12) !important;
    }}
    [data-testid="stAlert"] {{
        background: rgba(0,40,30,0.85) !important;
        border: 1px solid rgba(255,180,100,0.4) !important;
        border-radius: 12px !important;
        color: #f0f8f0 !important;
    }}
    .main .stCaption {{
        color: rgba(180,220,190,0.7) !important;
    }}
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
    .section-title {{
        color: #b8e6b8 !important;
        font-size: 1.15rem !important;
        margin-bottom: 1rem !important;
    }}
    
    /* ─── POST-IT SYSTEM ─── */
    .postit-modal {{
        display: none;
        position: fixed;
        z-index: 9999;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.6);
        backdrop-filter: blur(3px);
        animation: fadeIn 0.3s ease;
    }}
    
    .postit-modal:target {{
        display: block;
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    
    .postit-content {{
        position: relative;
        background: #fef3a8;
        background: linear-gradient(135deg, #fef3a8 0%, #f9e79f 100%);
        margin: 10% auto;
        padding: 2rem;
        width: 90%;
        max-width: 500px;
        border-radius: 2px;
        box-shadow: 
            0 1px 4px rgba(0,0,0,0.2),
            0 0 40px rgba(0,0,0,0.1) inset,
            5px 5px 15px rgba(0,0,0,0.3);
        color: #2c3e50 !important;
        font-family: 'Patrick Hand', 'Comic Sans MS', cursive !important;
        font-size: 1.1rem;
        line-height: 1.6;
        transform: rotate(-1deg);
        animation: slideIn 0.4s ease;
    }}
    
    .postit-content::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 30px;
        background: rgba(0,0,0,0.03);
        border-radius: 2px 2px 0 0;
    }}
    
    @keyframes slideIn {{
        from {{ transform: translateY(-50px) rotate(-3deg); opacity: 0; }}
        to {{ transform: translateY(0) rotate(-1deg); opacity: 1; }}
    }}
    
    .postit-content h3 {{
        color: #1a3025 !important;
        font-family: 'Patrick Hand', 'Comic Sans MS', cursive !important;
        font-size: 1.4rem !important;
        margin-bottom: 1rem !important;
        border-bottom: 2px solid rgba(0,0,0,0.1);
        padding-bottom: 0.5rem;
    }}
    
    .postit-content p {{
        color: #2c3e50 !important;
        font-family: 'Patrick Hand', 'Comic Sans MS', cursive !important;
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
    }}
    
    .postit-close {{
        position: absolute;
        top: 10px;
        right: 15px;
        color: #8b7355;
        font-size: 1.5rem;
        font-weight: bold;
        text-decoration: none;
        cursor: pointer;
        transition: color 0.2s;
        z-index: 10;
    }}
    
    .postit-close:hover {{
        color: #5d4e37;
    }}
    
    .term-link {{
        color: #ffd700 !important;
        text-decoration: underline;
        text-decoration-style: dotted;
        text-underline-offset: 3px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
        position: relative;
    }}
    
    .term-link:hover {{
        color: #ffed4a !important;
        text-shadow: 0 0 8px rgba(255,215,0,0.4);
    }}
    
    .definicion-texto {{
        font-size: 1.15rem !important;
        line-height: 1.9 !important;
        text-align: justify;
        color: #e8f5e9 !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

inject_css()

# ─────────────────────────────────────────────
# FUNCIÓN: Generar HTML de definición con post-its
# ─────────────────────────────────────────────
def generar_texto_definicion_ecologica():
    """Genera el texto de definición ecológica con hipervínculos a post-its"""
    
    texto = """
    <div class="definicion-texto">
    <p>Desde una perspectiva ecológica, los <strong>líquenes</strong> se definen como una 
    <a href="#postit-simbiosis" class="term-link">asociación simbiótica mutualista</a> 
    entre un hongo (micobionte) y uno o más organismos fotosintéticos (fotobiontes), 
    generalmente algas verdes o cianobacterias. Esta asociación no es meramente una 
    coexistencia casual, sino una integración funcional tan profunda que el conjunto 
    resultante —el talo liquénico— se comporta como un único organismo con propiedades 
    emergentes que ninguno de sus componentes posee por separado.</p>
    
    <p>El líquen representa, en esencia, un sistema <a href="#postit-estable" class="term-link">ecológicamente estable</a> 
    que ha perdurado a través de millones de años de evolución. Su estabilidad no implica 
    rigidez, sino una capacidad de mantener la homeostasis interna frente a fluctuaciones 
    ambientales significativas. Los líquenes demuestran una notable plasticidad fisiológica, 
    operando dentro de <a href="#postit-resiliencia" class="term-link">umbrales de resiliencia</a> 
    que les permiten sobrevivir en condiciones extremas —deserticas hasta antárticas— 
    donde organismos más complejos fracasan.</p>
    
    <p>A diferencia de las relaciones tróficas convencionales observadas en 
    <a href="#postit-troficos" class="term-link">niveles tróficos</a> clásicos, la simbiosis 
    liquénica trasciende la simple transferencia de energía. El fotobionte aporta carbohidratos 
    fotosintéticos al hongo, quien a su vez proporciona protección estructural, agua y 
    nutrientes minerales. Este intercambio simbiótico posiciona al líquen en una categoría 
    funcional única: no es un productor primario ni un consumidor en el sentido estricto, 
    sino una entidad híbrida que modifica radicalmente los flujos de materia y energía 
    en los ecosistemas donde habita.</p>
    
    <p>Contemporáneamente, la investigación ha revelado que los líquenes son 
    <a href="#postit-dinamicas" class="term-link">asociaciones dinámicas</a> cuya composición 
    microbiana varía según el contexto ambiental. No son entidades estáticas, sino sistemas 
    adaptativos que pueden incorporar bacterias, otros hongos y microorganismos según las 
    demandas ecológicas del hábitat. Esta dinamicidad desafía las definiciones taxonómicas 
    rígidas y enfatiza su naturaleza como consorcios biológicos en constante reconfiguración.</p>
    
    <p>En la visión más moderna, los líquenes se conceptualizan como un 
    <a href="#postit-holobionte" class="term-link">holobionte complejo</a>: una metaorganización 
    donde el hospedero fúngico y toda su microbiota asociada funcionan como una unidad 
    de selección natural. Esta perspectiva holobionte integra no solo al micobionte y 
    fotobionte principales, sino también a bacterias, arqueas, líquenes endofíticos y 
    virus que modulan la fisiología, ecología y evolución del conjunto. El líquen, 
    entonces, no es un organismo dual sino una comunidad funcional que ha alcanzado 
    un grado de integración tal que opera como individuo ecológico.</p>
    </div>
    """
    
    modales = ""
    terminos = [
        ("simbiosis", "asociación simbiótica mutualista"),
        ("estable", "ecológicamente estable"),
        ("resiliencia", "umbrales de resiliencia"),
        ("troficos", "niveles tróficos"),
        ("dinamicas", "asociaciones dinámicas"),
        ("holobionte", "holobionte complejo"),
    ]
    
    for id_suffix, clave in terminos:
        info = DEFINICIONES_POSTIT[clave]
        modal_html = (
            f'<div id="postit-{id_suffix}" class="postit-modal" '
            f'onclick="if(event.target == this){{window.location.hash=\'\';}}">'
            f'<div class="postit-content" onclick="event.stopPropagation();">'
            f'<a href="#" class="postit-close">&times;</a>'
            f'<h3>📌 {info["titulo"]}</h3>'
            f'<p>{info["definicion"]}</p>'
            f'</div></div>'
        )
        modales += modal_html
    
    return texto + modales

# ─────────────────────────────────────────────
# ESTADO DE SESIÓN
# ─────────────────────────────────────────────
if "vista" not in st.session_state:
    st.session_state.vista = "inicio"
if "subtema_activo" not in st.session_state:
    st.session_state.subtema_activo = None

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌿 Liquenología")
    st.markdown("---")

    if st.button("🏠 Inicio", key="btn_inicio", use_container_width=True):
        st.session_state.vista = "inicio"
        st.session_state.subtema_activo = None
        st.rerun()

    st.markdown("**📚 Categorías**")
    for cat_nombre in CATEGORIAS.keys():
        is_active = st.session_state.vista == cat_nombre
        label = f"**{cat_nombre}**" if is_active else cat_nombre
        if st.button(label, key=f"btn_cat_{cat_nombre}", use_container_width=True):
            st.session_state.vista = cat_nombre
            st.session_state.subtema_activo = None
            st.rerun()

    if st.session_state.vista in CATEGORIAS:
        st.markdown("---")
        cat_data = CATEGORIAS[st.session_state.vista]
        subtemas_list = list(cat_data.get("subtemas", {}).keys())
        nombre_cat = st.session_state.vista.split(" ", 1)[-1]
        st.markdown(f"**Subtemas — {nombre_cat}:**")
        for sub in subtemas_list:
            is_sub = st.session_state.subtema_activo == sub
            lbl = f"▶ {sub}" if is_sub else f"· {sub}"
            if st.button(lbl, key=f"btn_sub_{sub}", use_container_width=True):
                st.session_state.subtema_activo = None if is_sub else sub
                st.rerun()

    st.markdown("---")
    st.caption("Glosario Interactivo de Liquenología · v2.0")

# ─────────────────────────────────────────────
# VISTA: INICIO
# ─────────────────────────────────────────────
if st.session_state.vista == "inicio":
    st.title("🌿 Glosario Interactivo de Liquenología")
    st.markdown(
        '<p class="page-subtitle">Busca términos, explora el carrusel y navega por categorías</p>',
        unsafe_allow_html=True,
    )

    termino = st.text_input("", placeholder="🔍 Escribe un término del glosario", label_visibility="collapsed")
    if termino:
        termino_cap = termino.strip().capitalize()
        if termino_cap in glosario:
            info = glosario[termino_cap]
            st.markdown('<div class="glosario-result">', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(info["imagen"], use_container_width=True)
            with col2:
                st.markdown(f"### {termino_cap}")
                st.write(info["Descripción"])
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Ese término no está en el glosario.")

    st.markdown("---")
    st.markdown('<p class="section-title">Acerca del proyecto</p>', unsafe_allow_html=True)

    try:
        from streamlit_carousel import carousel
        imagenes_carrusel = [
            {"img": path_imagen("imagenes/Carrusel1.png"), "title": "", "text": ""},
            {"img": path_imagen("imagenes/Carrusel2.jpg"), "title": "", "text": ""},
            {"img": path_imagen("imagenes/Carrusel3.jpg"), "title": "", "text": ""},
            {"img": path_imagen("imagenes/Carrusel4.jpg"), "title": "", "text": ""},
        ]
        carousel(items=imagenes_carrusel, container_height=420)
    except ImportError:
        st.info("Instala streamlit-carousel para ver el carrusel: pip install streamlit-carousel")

    st.markdown("---")
    st.markdown("### 📚 Explora las categorías")
    cats = list(CATEGORIAS.keys())
    cols = st.columns(3)
    for i, cat in enumerate(cats):
        n = len(CATEGORIAS[cat].get("subtemas", {}))
        icon = cat.split(" ")[0]
        nombre = cat.split(" ", 1)[-1]
        with cols[i % 3]:
            st.markdown(f"**{icon} {nombre}**")
            st.caption(f"{n} subtemas")

# ─────────────────────────────────────────────
# VISTA: CATEGORÍA
# ─────────────────────────────────────────────
elif st.session_state.vista in CATEGORIAS:
    cat_actual = st.session_state.vista
    datos_cat = CATEGORIAS[cat_actual]
    subtemas = datos_cat.get("subtemas", {})
    subtema_actual = st.session_state.subtema_activo

    st.title(cat_actual)

    if subtema_actual is None:
        st.markdown(
            '<p class="page-subtitle">Selecciona un subtema en el menú lateral para explorar su contenido</p>',
            unsafe_allow_html=True,
        )
        st.markdown("---")
        st.markdown("#### Descripción general")
        st.markdown(
            f'<div class="desc-general">{datos_cat.get("descripcion_general", "")}</div>',
            unsafe_allow_html=True,
        )
        st.markdown("#### Subtemas de esta sección")
        cols = st.columns(2)
        for i, sub in enumerate(subtemas.keys()):
            with cols[i % 2]:
                st.markdown(f"- {sub}")
    else:
        info_sub = subtemas.get(subtema_actual, {})
        st.markdown("---")
        st.markdown('<div class="subtema-card">', unsafe_allow_html=True)
        st.markdown(f"## {subtema_actual}")
        
        # ─── CONTENIDO ESPECIAL: Definición Ecológica ───
        if subtema_actual == "Definición ecológica de los líquenes":
            st.markdown('<span class="placeholder-badge">📖 Contenido desarrollado</span>', unsafe_allow_html=True)
            
            html_definicion = generar_texto_definicion_ecologica()
            st.markdown(html_definicion, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("### 🔬 Implicaciones Ecológicas")
            st.markdown("""
            <div class="definicion-texto">
            <p>La definición ecológica del líquen subraya que no es un mero accidente evolutivo, 
            sino una estrategia biológica exitosa que ha colonizado prácticamente todos los 
            ecosistemas terrestres. Como <strong>pioneros ecológicos</strong>, los líquenes inician 
            la sucesión primaria en sustratos desnudos (roca, suelo volcánico, corteza recién 
            expuesta), contribuyendo a la formación de suelo mediante la acumulación de materia 
            orgánica y la lixiviación de minerales.</p>
            
            <p>Su función como <strong>indicadores ambientales</strong> deriva directamente de 
            esta definición ecológica: al ser organismos que integran múltiples componentes 
            biológicos en una sola entidad funcional, cualquier alteración en la calidad del aire, 
            agua o suelo se refleja de manera amplificada en su fisiología, crecimiento y 
            distribución. La sensibilidad del holobionte liquénico a los contaminantes atmosféricos 
            lo convierte en una herramienta de monitoreo ambiental sin paralelo en el reino vegetal.</p>
            
            <p>Finalmente, la naturaleza de <strong>asociación dinámica</strong> explica la 
            extraordinaria diversidad ecológica de los líquenes: un mismo micobionte puede asociarse 
            con diferentes fotobiontes según el hábitat, generando talos morfológicamente distintos 
            adaptados a condiciones lumínicas, hídricas y térmicas específicas. Esta plasticidad 
            simbiótica es, en sí misma, una innovación evolutiva que explica la persistencia y 
            radiación adaptativa de los líquenes a lo largo de más de 400 millones de años.</p>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.markdown('<span class="placeholder-badge">⏳ Contenido en desarrollo</span>', unsafe_allow_html=True)

            texto = info_sub.get("texto", "")
            if texto:
                st.markdown(texto)
            else:
                st.info(
                    "El contenido detallado de este subtema se añadirá próximamente. "
                    "Aquí aparecerán textos, imágenes, videos y diagramas de apoyo."
                )

        imagenes = info_sub.get("imagenes", [])
        if imagenes:
            st.markdown("#### 🖼️ Imágenes")
            cols_img = st.columns(min(len(imagenes), 3))
            for j, img_path in enumerate(imagenes):
                with cols_img[j % 3]:
                    st.image(img_path, use_container_width=True)

        videos = info_sub.get("videos", [])
        if videos:
            st.markdown("#### 🎬 Videos")
            for vid in videos:
                st.video(vid)

        diagramas = info_sub.get("diagramas", [])
        if diagramas:
            st.markdown("#### 📊 Diagramas")
            for diag in diagramas:
                st.image(diag, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")

        if st.button("← Volver a la descripción general"):
            st.session_state.subtema_activo = None
            st.rerun()