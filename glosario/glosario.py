import streamlit as st
import streamlit.components.v1 as components
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
    "simbiosis": {
        "titulo": "Asociación Simbiótica Mutualista",
        "definicion": (
            "Relación biológica íntima y duradera entre dos organismos de especies diferentes "
            "(hongo + alga/cianobacteria) donde ambos se benefician: el hongo proporciona estructura, "
            "protección y nutrientes, mientras el fotobionte aporta carbohidratos mediante fotosíntesis. "
            "Es la base de la organización del talo liquénico."
        ),
    },
    "estable": {
        "titulo": "Ecológicamente Estable",
        "definicion": (
            "Condición de un sistema o asociación que mantiene sus propiedades estructurales y "
            "funcionales a lo largo del tiempo frente a perturbaciones ambientales normales. "
            "En líquenes, implica la persistencia de la simbiosis sin desintegración del talo bajo "
            "condiciones ambientales variables."
        ),
    },
    "resiliencia": {
        "titulo": "Umbrales de Resiliencia",
        "definicion": (
            "Límites críticos de perturbación ambiental (humedad, temperatura, radiación, contaminantes) "
            "que un ecosistema u organismo puede tolerar antes de sufrir un cambio cualitativo irreversible. "
            "Los líquenes poseen umbrales amplios gracias a su poiquilohidria y metabolismo flexible."
        ),
    },
    "troficos": {
        "titulo": "Niveles Tróficos",
        "definicion": (
            "Posiciones que ocupan los organismos en una cadena alimentaria según su fuente de energía "
            "y nutrientes. En líquenes, el fotobionte ocupa el nivel productor (autótrofo), mientras "
            "el micobionte es heterótrofo; juntos conforman una unidad funcional que interactúa con "
            "otros niveles del ecosistema."
        ),
    },
    "dinamicas": {
        "titulo": "Asociaciones Dinámicas",
        "definicion": (
            "Interacciones biológicas que cambian en intensidad, especificidad o composición a lo "
            "largo del tiempo o según condiciones ambientales. Los líquenes presentan asociaciones "
            "dinámicas porque pueden modificar la proporción hongo-alga, incorporar nuevos simbiontes "
            "o ajustar su fisiología según el hábitat."
        ),
    },
    "holobionte": {
        "titulo": "Holobionte Complejo",
        "definicion": (
            "Entidad biológica que funciona como un solo organismo pero está compuesta por el "
            "hospedero (hongo liquénico) y toda su microbiota asociada (algas, cianobacterias, "
            "bacterias, líquenes endofíticos y otros microorganismos), interactuando como una unidad "
            "de selección ecológica y evolutiva."
        ),
    },
}

# ─────────────────────────────────────────────
# DATOS: categorías y subtemas
# ─────────────────────────────────────────────
CATEGORIAS = {
    "🔬 Anatomía y Morfología": {
        "descripcion_general": (
            "La anatomía y morfología de los líquenes abarca el estudio de su forma externa e interna, "
            "desde la organización del talo liquénico hasta las estructuras reproductivas. "
            "Esta disciplina es fundamental para la identificación, clasificación y comprensión "
            "de la diversidad liquénica."
        ),
        "subtemas": {
            "Morfología externa": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Definición del talo liquénico": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Retención de agua": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Resistencia a la radiación": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Colonización de sustratos": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Tipos de corteza": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Tipos de talo": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Características externas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Anatomía interna y organización tisular": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Variaciones anatómicas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Capa algal": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Médula": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Estructuras reproductivas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🌱 Ecología": {
        "descripcion_general": (
            "La ecología de los líquenes estudia sus relaciones con el ambiente y otros organismos. "
            "Son organismos altamente adaptados a condiciones extremas y cumplen roles ecológicos "
            "fundamentales en los ecosistemas donde habitan, desde la fijación de nitrógeno "
            "hasta la formación de suelos."
        ),
        "subtemas": {
            "Introducción y bases ecológicas de los líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Definición ecológica de los líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Hipótesis 'Everything is everywhere, but the environment selects'": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Funciones bacterianas en los líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Hábitats de los líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Tipos de líquenes según el lugar en donde se encuentren": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Adaptaciones ecológicas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Roles ecológicos de los líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Líquenes como pioneros": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Ciclos biogeoquímicos": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Interacciones con fauna": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Indicadoras ambientales": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Líquenes y cambio ambiental": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Métodos de estudio y recolecta": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Teoría del continuum": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🧬 Evolución": {
        "descripcion_general": (
            "El estudio evolutivo de los líquenes explora el origen y diversificación de la simbiosis "
            "liquénica a lo largo del tiempo geológico. La evidencia fósil, molecular y los patrones "
            "de coespeciación revelan una historia evolutiva compleja y fascinante."
        ),
        "subtemas": {
            "Origen evolutivo de la liquenización y la simbiosis liquénica": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Definición evolutiva del líquen": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Asociaciones intermedias de la liquenización y otros organismos asociados": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Evidencia fósil, molecular, Eventos de liquenización, Deliquenización y Reliquenización": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Coespeciación y cospeciación": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Cleptobiosis": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Procesos macro y microevolutivos en los líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🗺️ Biogeografía": {
        "descripcion_general": (
            "La biogeografía liquénica analiza los patrones de distribución geográfica de los líquenes "
            "y los procesos históricos y ecológicos que los explican. Elementos como el Mar de Tetis "
            "han jugado un papel clave en la distribución actual de muchas especies."
        ),
        "subtemas": {
            "Distribución según la región": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "El Mar de Tetis": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "📜 Historia": {
        "descripcion_general": (
            "La historia de la liquenología abarca desde las primeras observaciones antes de Cristo "
            "hasta los estudios modernos. Figuras como Erik Acharius y Nylander marcaron hitos "
            "fundamentales en el desarrollo de esta ciencia."
        ),
        "subtemas": {
            "Los líquenes antes de Cristo": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Edad Media": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Estudios de los líquenes antes de Acharius": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Erick Acharius el padre de la liquenología": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Antes de Nylander": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Inglaterra y Francia, Nylander y el descontento con la escuela Italiana": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Los efectos de la influencia de Nylander": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Estudios de la liquenología en la actualidad": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "⚗️ Metabolitos Secundarios": {
        "descripcion_general": (
            "Los metabolitos secundarios liquénicos son compuestos químicos únicos producidos por "
            "la simbiosis. Su estudio abarca desde las rutas biosintéticas hasta su detección "
            "y aplicaciones potenciales en medicina y biotecnología."
        ),
        "subtemas": {
            "Origen de los metabolitos secundarios": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Rutas biosintéticas principales": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Poliquétidos y enzimas PKS": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Estudios moleculares y expresión heteróloga": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Detección de metabolitos": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🍃 Metabolismo y Nutrición": {
        "descripcion_general": (
            "El metabolismo y nutrición de los líquenes comprende los procesos de intercambio de agua, "
            "carbono, nitrógeno y minerales en la simbiosis. Su entendimiento es clave para comprender "
            "cómo estos organismos sobreviven en ambientes extremos."
        ),
        "subtemas": {
            "Arquitectura y flujo apoplástico, Hidrofobinas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Poiquilohidria, ventanas de actividad y dominancia en extremos": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Fotobiontes y hábitat": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Sequía, cavitación y mecánica de pared": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Cuerpos concéntricos": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Nucleación de hielo": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Fotosíntesis y respiración": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Resistencia a la difusión y su relación con la humedad": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Modos de rehidratación": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Balance fotosíntesis-respiración": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Asignación de recursos en la simbiosis": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Tendencias entre líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Translocación del carbono": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Sumideros de carbono": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Importancia del nitrógeno": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Líquenes y formas de nitrógeno": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Metabolismo del nitrógeno": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Relación cefalodios-talo": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Exceso de nitrógeno": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Patrones diarios de fijación y factores ambientales": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Propiedades físicas y químicas de minerales y otros elementos": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Dependencias atmosféricas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Otros requerimientos nutricionales": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Mecanismos de acumulación": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Fuentes de nutrientes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Compartimentalización": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Toxicidad por metales": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🌀 Morfogénesis del Talo": {
        "descripcion_general": (
            "La morfogénesis del talo estudia cómo se desarrolla y diferencia la estructura del líquen "
            "desde sus componentes simbióticos hasta el talo maduro. Involucra procesos de reconocimiento, "
            "inducción de fenotipos y diferenciación tisular."
        ),
        "subtemas": {
            "Particularidades de la simbiosis liquénica": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Macro y microlíquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Reconocimiento y especificidad": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Propágulos simbióticos": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Pretalo como etapa intermedia": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Inducción de fenotipos simbióticos": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Diferenciación del talo estratificado": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Morfología funcional del talo maduro": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Regulación y plasticidad": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Líquenes bipartitas y tripartitas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Secreción y síntesis de pared en Ramalina menziesii": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🔁 Reproducción": {
        "descripcion_general": (
            "La reproducción liquénica engloba tanto estrategias sexuales como asexuales. "
            "El debate actual sobre la relevancia de cada modo reproductivo y la diversidad "
            "de estructuras involucradas hacen de este tema uno de los más dinámicos en la liquenología."
        ),
        "subtemas": {
            "Reproducción sexual": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Contexto genético en líquenes": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Debate actual": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Los líquenes foliícolas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Diversidad de estructuras reproductivas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Morfogénesis de los soredios": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Morfogénesis de los isidios": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Morfogénesis del Peritecio": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
    "🏷️ Sistemática y Taxonomía": {
        "descripcion_general": (
            "La sistemática y taxonomía liquénica organiza la diversidad de líquenes en un sistema "
            "clasificatorio coherente. Desde los conceptos de especie hasta los géneros más "
            "representativos en México, esta disciplina integra morfología, química y filogenia."
        ),
        "subtemas": {
            "Conceptos clave en sistemática": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Conceptos alternativos a especie taxonómica": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Caracteres usados en sistemática": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Cromatografía en Capa Fina": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Principales órdenes y familias": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Claves interpretativas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Géneros más representativos en México": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Retos en sistemática": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Sistemática y conservación": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Evaluación de especies amenazadas": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
            "Sistemática y biogeografía": {"texto": "", "imagenes": [], "videos": [], "diagramas": []},
        },
    },
}

# ─────────────────────────────────────────────
# CSS GLOBAL + POST-ITS (compatible con Edge / Chromium / Firefox / Safari)
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
        color: #ffffff !important;
        font-family: 'Source Sans 3', sans-serif;
        line-height: 1.7;
        font-size: 1.05rem !important;
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

    /* ─────────────────────────────────────────────
       Subtemas como botones (vista de categoría)
       ───────────────────────────────────────────── */
    .subtema-grid .stButton > button {{
        background: rgba(10,55,35,0.85) !important;
        border: 1px solid rgba(120,200,150,0.35) !important;
        color: #e6f5ea !important;
        font-family: 'Source Sans 3', sans-serif !important;
        font-size: 0.95rem !important;
        text-align: left !important;
        padding: 0.85rem 1rem !important;
        border-radius: 12px !important;
        width: 100% !important;
        transition: all 0.2s ease;
        box-shadow: 0 4px 14px rgba(0,0,0,0.25);
        white-space: normal !important;
        line-height: 1.35 !important;
        height: auto !important;
        min-height: 3.2rem;
    }}
    .subtema-grid .stButton > button:hover {{
        background: rgba(20,90,55,0.95) !important;
        border-color: rgba(180,230,180,0.7) !important;
        transform: translateY(-1px);
        box-shadow: 0 6px 18px rgba(0,0,0,0.35);
    }}

    /* ─────────────────────────────────────────────
       POST-IT MODAL con <details>/<summary>.
       - <details> es HTML nativo (no se sanea, no usa
         <input> ni :target, funciona en Edge).
       - Solo se muestra un post-it a la vez (atributo
         name="postit" + JS de respaldo).
       - El post-it abierto se renderiza como modal
         centrado con fondo oscuro (no empuja el texto).
       ───────────────────────────────────────────── */
    .definicion-texto .prose-p {{
        font-size: 1.07rem;
        line-height: 1.85;
        text-align: justify;
        color: #e8f5e9;
        margin: 0 0 1rem 0;
    }}
    .definicion-texto .prose-p strong {{
        color: #ffffff;
    }}
    .term-detail {{
        display: inline;
    }}
    .term-detail > summary.term-link {{
        display: inline;
        list-style: none;
        cursor: pointer;
        color: #ffd700;
        text-decoration: underline;
        text-decoration-style: dotted;
        text-underline-offset: 3px;
        font-weight: 600;
        transition: color 0.2s, text-shadow 0.2s;
    }}
    .term-detail > summary.term-link::-webkit-details-marker {{
        display: none;
    }}
    .term-detail > summary.term-link::marker {{
        content: "";
        display: none;
    }}
    .term-detail > summary.term-link:hover {{
        color: #ffed4a;
        text-shadow: 0 0 8px rgba(255,215,0,0.45);
    }}
    .term-detail .postit-modal {{
        display: none;
    }}
    .term-detail[open] > .postit-modal {{
        display: block;
        position: fixed;
        inset: 0;
        width: 100%;
        height: 100%;
        z-index: 99998;
        background: rgba(0,0,0,0.6);
        -webkit-backdrop-filter: blur(3px);
        backdrop-filter: blur(3px);
        animation: fadeIn 0.2s ease;
        cursor: pointer;
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to   {{ opacity: 1; }}
    }}
    .term-detail[open] > .postit-modal > .postit-content {{
        display: block;
        position: fixed;
        top: 50%;
        left: 50%;
        z-index: 99999;
        width: min(520px, 90vw);
        max-height: 80vh;
        overflow-y: auto;
        padding: 1.8rem 2.2rem;
        background: #fef3a8;
        background: linear-gradient(135deg, #fef3a8 0%, #f9e79f 100%);
        color: #2c3e50;
        font-family: 'Patrick Hand', 'Comic Sans MS', cursive;
        font-size: 1.1rem;
        line-height: 1.6;
        border-radius: 3px;
        text-align: left;
        white-space: normal;
        cursor: default;
        transform: translate(-50%, -50%) rotate(-1.4deg);
        box-shadow:
            0 1px 4px rgba(0,0,0,0.25),
            0 0 40px rgba(0,0,0,0.12) inset,
            6px 6px 26px rgba(0,0,0,0.5);
        animation: postitIn 0.3s ease;
    }}
    @keyframes postitIn {{
        from {{ opacity: 0; transform: translate(-50%, -50%) rotate(-4deg) scale(0.92); }}
        to   {{ opacity: 1; transform: translate(-50%, -50%) rotate(-1.4deg) scale(1); }}
    }}
    .postit-content .postit-title {{
        display: block;
        color: #1a3025;
        font-family: 'Patrick Hand', 'Comic Sans MS', cursive;
        font-size: 1.4rem;
        font-weight: bold;
        margin: 0 0 0.7rem 0;
        padding: 0 2rem 0.5rem 0;
        border-bottom: 2px solid rgba(0,0,0,0.12);
    }}
    .postit-content .postit-body {{
        display: block;
        color: #2c3e50;
        font-family: 'Patrick Hand', 'Comic Sans MS', cursive;
        font-size: 1.1rem;
        line-height: 1.65;
    }}
    .postit-content .postit-close {{
        position: absolute;
        top: 8px;
        right: 14px;
        width: 32px;
        height: 32px;
        line-height: 28px;
        text-align: center;
        font-size: 1.6rem;
        font-weight: bold;
        color: #8b7355;
        cursor: pointer;
        user-select: none;
        border-radius: 50%;
        transition: background 0.15s, color 0.15s, transform 0.2s;
        z-index: 2;
    }}
    .postit-content .postit-close:hover {{
        color: #5d4e37;
        background: rgba(0,0,0,0.1);
        transform: rotate(90deg);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

inject_css()

# ─────────────────────────────────────────────
# FUNCIÓN: Generar HTML de definición con post-its
# Usa <details>/<summary> (HTML nativo). Funciona en
# Edge, Chrome, Firefox y Safari sin JS. No depende
# de <input> (que Streamlit sanea) ni de :target
# (que Streamlit intercepta).
# ─────────────────────────────────────────────
def term(k, label):
    """Genera un término clickable que despliega un modal con su definición.

    Estructura:
      <details name="postit">           ← el atributo `name` agrupa todos los
        <summary>término</summary>         post-its: al abrir uno, los navegadores
        <span class="postit-modal">        modernos cierran los demás automáticamente.
          <span class="postit-content">  ← post-it amarillo (no se cierra al
            <span class="postit-close">     hacer clic dentro)
            <span class="postit-title">
            <span class="postit-body">
    """
    info = DEFINICIONES_POSTIT[k]
    return (
        f'<details class="term-detail" name="postit">'
        f'<summary class="term-link">{label}</summary>'
        f'<span class="postit-modal">'
        f'<span class="postit-content">'
        f'<span class="postit-close" role="button" aria-label="Cerrar" title="Cerrar">&times;</span>'
        f'<span class="postit-title">📌 {info["titulo"]}</span>'
        f'<span class="postit-body">{info["definicion"]}</span>'
        f'</span>'
        f'</span>'
        f'</details>'
    )


def inyectar_handler_cerrar_postit():
    """Inyecta el JS de control de post-its vía iframe.

    Responsabilidades:
      1. Cerrar el post-it activo al hacer clic en la "×".
      2. Cerrar al hacer clic en el fondo oscuro (.postit-modal) sin afectar
         clics dentro del .postit-content.
      3. Cerrar con la tecla Escape.
      4. Garantizar exclusividad (un solo post-it abierto) incluso en
         navegadores que aún no implementen el atributo `name` en <details>.
    """
    components.html(
        """
        <script>
        (function () {
          const doc = window.parent && window.parent.document;
          if (!doc || doc.__postitHandlerAttached) return;
          doc.__postitHandlerAttached = true;

          function cerrarTodos() {
            doc.querySelectorAll('details.term-detail[open]').forEach(function (d) {
              d.removeAttribute('open');
            });
          }

          doc.addEventListener('click', function (e) {
            const t = e.target;
            if (!t) return;

            const closeBtn = t.closest && t.closest('.postit-close');
            if (closeBtn) {
              const d = closeBtn.closest('details.term-detail');
              if (d) {
                d.removeAttribute('open');
                e.preventDefault();
                e.stopPropagation();
              }
              return;
            }

            const inContent = t.closest && t.closest('.postit-content');
            if (inContent) return;

            const inModal = t.closest && t.closest('.postit-modal');
            if (inModal) {
              const d = inModal.closest('details.term-detail');
              if (d) {
                d.removeAttribute('open');
                e.preventDefault();
                e.stopPropagation();
              }
              return;
            }

            const summary = t.closest && t.closest('summary.term-link');
            if (!summary) {
              cerrarTodos();
            }
          }, true);

          doc.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
              cerrarTodos();
            }
          });

          doc.addEventListener('toggle', function (e) {
            const d = e.target;
            if (!d || !d.classList || !d.classList.contains('term-detail')) return;
            if (!d.open) return;
            doc.querySelectorAll('details.term-detail[open]').forEach(function (other) {
              if (other !== d) other.removeAttribute('open');
            });
          }, true);
        })();
        </script>
        """,
        height=0,
    )

def generar_texto_definicion_ecologica():
    parrafos = [
        (
            'Desde una perspectiva ecológica, los <strong>líquenes</strong> se definen como una '
            + term("simbiosis", "asociación simbiótica mutualista")
            + ' entre un hongo (micobionte) y uno o más organismos fotosintéticos (fotobiontes), '
            'generalmente algas verdes o cianobacterias. Esta asociación no es meramente una '
            'coexistencia casual, sino una integración funcional tan profunda que el conjunto '
            'resultante —el talo liquénico— se comporta como un único organismo con propiedades '
            'emergentes que ninguno de sus componentes posee por separado.'
        ),
        (
            'El líquen representa, en esencia, un sistema '
            + term("estable", "ecológicamente estable")
            + ' que ha perdurado a través de millones de años de evolución. Su estabilidad no implica '
            'rigidez, sino una capacidad de mantener la homeostasis interna frente a fluctuaciones '
            'ambientales significativas. Los líquenes demuestran una notable plasticidad fisiológica, '
            'operando dentro de '
            + term("resiliencia", "umbrales de resiliencia")
            + ' que les permiten sobrevivir en condiciones extremas —desérticas hasta antárticas— '
            'donde organismos más complejos fracasan.'
        ),
        (
            'A diferencia de las relaciones tróficas convencionales observadas en '
            + term("troficos", "niveles tróficos")
            + ' clásicos, la simbiosis liquénica trasciende la simple transferencia de energía. '
            'El fotobionte aporta carbohidratos fotosintéticos al hongo, quien a su vez proporciona '
            'protección estructural, agua y nutrientes minerales. Este intercambio simbiótico '
            'posiciona al líquen en una categoría funcional única: no es un productor primario ni '
            'un consumidor en el sentido estricto, sino una entidad híbrida que modifica radicalmente '
            'los flujos de materia y energía en los ecosistemas donde habita.'
        ),
        (
            'Contemporáneamente, la investigación ha revelado que los líquenes son '
            + term("dinamicas", "asociaciones dinámicas")
            + ' cuya composición microbiana varía según el contexto ambiental. No son entidades '
            'estáticas, sino sistemas adaptativos que pueden incorporar bacterias, otros hongos y '
            'microorganismos según las demandas ecológicas del hábitat. Esta dinamicidad desafía '
            'las definiciones taxonómicas rígidas y enfatiza su naturaleza como consorcios '
            'biológicos en constante reconfiguración.'
        ),
        (
            'En la visión más moderna, los líquenes se conceptualizan como un '
            + term("holobionte", "holobionte complejo")
            + ': una metaorganización donde el hospedero fúngico y toda su microbiota asociada '
            'funcionan como una unidad de selección natural. Esta perspectiva holobionte integra '
            'no solo al micobionte y fotobionte principales, sino también a bacterias, arqueas, '
            'líquenes endofíticos y virus que modulan la fisiología, ecología y evolución del '
            'conjunto. El líquen, entonces, no es un organismo dual sino una comunidad funcional '
            'que ha alcanzado un grado de integración tal que opera como individuo ecológico.'
        ),
    ]

    # Sin indentación al inicio de cada línea para evitar que Markdown
    # interprete los párrafos como bloques de código.
    cuerpo = "".join(f'<div class="prose-p">{p}</div>' for p in parrafos)
    return f'<div class="definicion-texto">{cuerpo}</div>'

# ─────────────────────────────────────────────
# ESTADO DE SESIÓN
# ─────────────────────────────────────────────
if "vista" not in st.session_state:
    st.session_state.vista = "inicio"
if "subtema_activo" not in st.session_state:
    st.session_state.subtema_activo = None

def ir_a_categoria(cat: str):
    st.session_state.vista = cat
    st.session_state.subtema_activo = None

def ir_a_subtema(cat: str, sub: str):
    st.session_state.vista = cat
    st.session_state.subtema_activo = sub

def ir_a_inicio():
    st.session_state.vista = "inicio"
    st.session_state.subtema_activo = None

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌿 Liquenología")
    st.markdown("---")

    st.button(
        "🏠 Inicio",
        key="btn_inicio",
        use_container_width=True,
        on_click=ir_a_inicio,
    )

    st.markdown("**📚 Categorías**")
    for cat_nombre in CATEGORIAS.keys():
        is_active = st.session_state.vista == cat_nombre
        label = f"**{cat_nombre}**" if is_active else cat_nombre
        st.button(
            label,
            key=f"btn_cat_{cat_nombre}",
            use_container_width=True,
            on_click=ir_a_categoria,
            args=(cat_nombre,),
        )

    if st.session_state.vista in CATEGORIAS:
        st.markdown("---")
        cat_data = CATEGORIAS[st.session_state.vista]
        subtemas_list = list(cat_data.get("subtemas", {}).keys())
        nombre_cat = st.session_state.vista.split(" ", 1)[-1]
        st.markdown(f"**Subtemas — {nombre_cat}:**")
        for sub in subtemas_list:
            is_sub = st.session_state.subtema_activo == sub
            lbl = f"▶ {sub}" if is_sub else f"· {sub}"
            st.button(
                lbl,
                key=f"btn_sub_{st.session_state.vista}_{sub}",
                use_container_width=True,
                on_click=ir_a_subtema,
                args=(st.session_state.vista, sub),
            )

    st.markdown("---")
    st.caption("Glosario Interactivo de Liquenología · v2.1")

# ─────────────────────────────────────────────
# VISTA: INICIO
# ─────────────────────────────────────────────
if st.session_state.vista == "inicio":
    st.title("🌿 Glosario Interactivo de Liquenología")
    st.markdown(
        '<p class="page-subtitle">Busca términos, explora el carrusel y navega por categorías</p>',
        unsafe_allow_html=True,
    )

    termino = st.text_input(
        "",
        placeholder="🔍 Escribe un término del glosario",
        label_visibility="collapsed",
    )
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
            st.button(
                f"{icon} {nombre}\n\n{n} subtemas",
                key=f"home_cat_{cat}",
                use_container_width=True,
                on_click=ir_a_categoria,
                args=(cat,),
            )

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
            '<p class="page-subtitle">Selecciona un subtema para explorar su contenido</p>',
            unsafe_allow_html=True,
        )
        st.markdown("---")
        st.markdown("#### Descripción general")
        st.markdown(
            f'<div class="desc-general">{datos_cat.get("descripcion_general", "")}</div>',
            unsafe_allow_html=True,
        )

        st.markdown("#### Subtemas de esta sección")
        st.markdown('<div class="subtema-grid">', unsafe_allow_html=True)
        sub_keys = list(subtemas.keys())
        cols = st.columns(2)
        for i, sub in enumerate(sub_keys):
            with cols[i % 2]:
                st.button(
                    sub,
                    key=f"main_sub_{cat_actual}_{sub}",
                    use_container_width=True,
                    on_click=ir_a_subtema,
                    args=(cat_actual, sub),
                )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        info_sub = subtemas.get(subtema_actual, {})
        st.markdown("---")
        st.markdown('<div class="subtema-card">', unsafe_allow_html=True)
        st.markdown(f"## {subtema_actual}")

        if subtema_actual == "Definición ecológica de los líquenes":
            st.markdown(
                '<span class="placeholder-badge">📖 Contenido desarrollado</span>',
                unsafe_allow_html=True,
            )

            html_definicion = generar_texto_definicion_ecologica()
            st.markdown(html_definicion, unsafe_allow_html=True)
            inyectar_handler_cerrar_postit()

            st.markdown("---")
            st.markdown("### 🔬 Implicaciones Ecológicas")
            implicaciones_html = (
                '<div class="definicion-texto">'
                '<div class="prose-p">La definición ecológica del líquen subraya que no es un mero '
                'accidente evolutivo, sino una estrategia biológica exitosa que ha colonizado '
                'prácticamente todos los ecosistemas terrestres. Como <strong>pioneros ecológicos'
                '</strong>, los líquenes inician la sucesión primaria en sustratos desnudos (roca, '
                'suelo volcánico, corteza recién expuesta), contribuyendo a la formación de suelo '
                'mediante la acumulación de materia orgánica y la lixiviación de minerales.</div>'
                '<div class="prose-p">Su función como <strong>indicadores ambientales</strong> '
                'deriva directamente de esta definición ecológica: al ser organismos que integran '
                'múltiples componentes biológicos en una sola entidad funcional, cualquier alteración '
                'en la calidad del aire, agua o suelo se refleja de manera amplificada en su '
                'fisiología, crecimiento y distribución. La sensibilidad del holobionte liquénico a '
                'los contaminantes atmosféricos lo convierte en una herramienta de monitoreo '
                'ambiental sin paralelo en el reino vegetal.</div>'
                '<div class="prose-p">Finalmente, la naturaleza de <strong>asociación dinámica'
                '</strong> explica la extraordinaria diversidad ecológica de los líquenes: un mismo '
                'micobionte puede asociarse con diferentes fotobiontes según el hábitat, generando '
                'talos morfológicamente distintos adaptados a condiciones lumínicas, hídricas y '
                'térmicas específicas. Esta plasticidad simbiótica es, en sí misma, una innovación '
                'evolutiva que explica la persistencia y radiación adaptativa de los líquenes a lo '
                'largo de más de 400 millones de años.</div>'
                '</div>'
            )
            st.markdown(implicaciones_html, unsafe_allow_html=True)
        else:
            st.markdown(
                '<span class="placeholder-badge">⏳ Contenido en desarrollo</span>',
                unsafe_allow_html=True,
            )

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

        st.button(
            "← Volver a la descripción general",
            key=f"back_{cat_actual}",
            on_click=ir_a_categoria,
            args=(cat_actual,),
        )
