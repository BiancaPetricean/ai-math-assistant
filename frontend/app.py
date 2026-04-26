import streamlit as st
import requests
import sympy as sp
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import random
import pandas as pd
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2 # type: ignore
import tempfile
import re

# configurare pagină
st.set_page_config(
    page_title="AI Math Tutor",
    page_icon="🧠",
    layout="wide"
)

# STIL PROFESIONAL
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.stButton>button {
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
}
.stTextInput>div>div>input {
    border-radius: 10px;
}
h1, h2, h3 {
    color: #2E86C1;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stButton>button:hover {
    background-color:#2E86C1;
    color:white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
}
</style>
""", unsafe_allow_html=True)

# =========================
# NAVIGARE
# =========================

st.sidebar.title("🧠 AI Math Tutor")

page = st.sidebar.radio(
"Navigare",
["Solver matematic","Generator exerciții","Simulare examen","Dashboard"]
)


# =========================
# DASHBOARD
# =========================

if page == "Dashboard":

    st.title("📊 Dashboard AI Math Tutor")
    st.caption("Vizualizare rapidă a activității utilizatorului")
    
    st.markdown("Analiza utilizării platformei")

    st.markdown("---")

    # CARDURI STATISTICE

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("📘 Exerciții rezolvate",154)
    col2.metric("📈 Funcții analizate",42)
    col3.metric("📝 Teste completate",15)
    col4.metric("🔢 Sisteme rezolvate",27)

    st.markdown("---")

    # DISTRIBUTIE EXERCITII

    st.subheader("📚 Tipuri de exerciții rezolvate")

    exercise_data = {
        "tip":["Aritmetică","Ecuații","Funcții","Derivate","Integrale","Geometrie"],
        "numar":[45,32,21,18,15,23]
    }

    df = pd.DataFrame(exercise_data)

    fig = px.pie(
        df,
        names="tip",
        values="numar",
        hole=0.5
    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown("---")

    # ACTIVITATE

    st.subheader("📈 Activitate utilizator")

    activity_data = {
        "zi":["Luni","Marți","Miercuri","Joi","Vineri","Sâmbătă","Duminică"],
        "exercitii":[6,9,14,7,11,5,3]
    }

    df2 = pd.DataFrame(activity_data)

    fig2 = px.line(
        df2,
        x="zi",
        y="exercitii",
        markers=True
    )

    st.plotly_chart(px.pie(df, names="tip", values="numar", hole=0.4), use_container_width=True)

    st.markdown("---")

    # PROGRES

    st.subheader("🏆 Progres capitole")

    progress_data = {
        "capitol":["Ecuații","Funcții","Derivate","Integrale","Geometrie"],
        "progres":[80,65,45,30,72]
    }

    df3 = pd.DataFrame(progress_data)

    fig3 = px.bar(
        df3,
        x="capitol",
        y="progres"
    )

    st.plotly_chart(fig3,use_container_width=True)
    
    # =========================
# SIMULARE EXAMEN
# =========================

if page == "Simulare examen":

    st.title("📝 Simulare examen matematic")

    st.markdown("Testează-ți cunoștințele")

    test_exercises = [

    {"question":"Rezolvați ecuația: x² - 5x + 6 = 0","answer":"2,3"},

    {"question":"Calculați derivata funcției f(x)=x³ - 2x","answer":"3*x**2-2"},

    {"question":"Calculați integrala ∫x² dx","answer":"x**3/3"},

    {"question":"Calculați sin(pi/2)","answer":"1"},

    {"question":"Calculați limita (x²-1)/(x-1) când x→1","answer":"2"}

    ]

    answers = []

    for i,ex in enumerate(test_exercises):

        st.subheader(f"Exercițiul {i+1}")

        st.write(ex["question"])

        ans = st.text_input("Răspuns",key=f"test{i}")

        answers.append(ans)

    if st.button("Verifică testul"):

        score = 0

        st.markdown("---")

        for i,ex in enumerate(test_exercises):

            if answers[i] == ex["answer"]:

                st.success(f"Exercițiul {i+1} corect")
                score += 1

            else:

                st.error(f"Exercițiul {i+1} greșit")

        st.markdown("---")

        st.subheader(f"🏆 Scor final: {score} / {len(test_exercises)}")

        procent = (score/len(test_exercises))*100

        st.progress(int(procent))
        
        # =========================
# GENERATOR EXERCITII
# =========================

if page == "Generator exerciții":

    st.title("🎲 Generator infinit de exerciții")

    nivel = st.selectbox(
    "Nivel",
    ["Clasele 1-4","Clasele 5-8","Clasele 9-12"]
    )

    tip = st.selectbox(
    "Tip exercițiu",
    [
    "Aritmetică",
    "Ecuații",
    "Sisteme de ecuații",
    "Funcții",
    "Derivate",
    "Integrale",
    "Limite",
    "Trigonometrie",
    "Geometrie"
    ]
    )

    if st.button("Generează exercițiu"):

        if tip == "Aritmetică":

            a = random.randint(1,100)
            b = random.randint(1,100)

            exercise = f"{a} + {b}"
            answer = str(a+b)

        elif tip == "Ecuații":

            a = random.randint(1,5)
            b = random.randint(1,10)

            exercise = f"{a}*x + {b} = 0"
            answer = str(-b/a)

        elif tip == "Sisteme de ecuații":

            a = random.randint(1,5)
            b = random.randint(1,5)

            exercise = f"""
            x + y = {a}
            x - y = {b}
            """

            x_val = (a+b)/2
            y_val = (a-b)/2

            answer = f"x={x_val}, y={y_val}"

        elif tip == "Funcții":

            n = random.randint(2,4)

            exercise = f"f(x) = x^{n} - 3x"

            answer = "Analiză funcție"

        elif tip == "Derivate":

            n = random.randint(2,5)

            exercise = f"f(x) = x^{n}"

            answer = f"{n}x^{n-1}"

        elif tip == "Integrale":

            n = random.randint(1,4)

            exercise = f"∫ x^{n} dx"

            answer = f"x^{n+1}/{n+1}"

        elif tip == "Limite":

            exercise = "(x^2 - 1)/(x - 1) când x→1"
            answer = "2"

        elif tip == "Trigonometrie":

            exercise = "sin(π/2)"
            answer = "1"

        elif tip == "Geometrie":

            r = random.randint(1,10)

            exercise = f"Aria cercului cu raza {r}"

            answer = f"{np.pi*r*r}"

        st.session_state.exercise = exercise
        st.session_state.answer = answer

    if "exercise" in st.session_state:

        st.markdown("---")

        st.subheader("Exercițiu")

        st.write(st.session_state.exercise)

        user_answer = st.text_input("Răspuns")

        if st.button("Verifică"):

            if user_answer == st.session_state.answer:

                st.success("✔ Corect")

            else:

                st.error("Greșit")

                st.write("Răspuns corect:",st.session_state.answer)

# =========================
# SOLVER
# =========================

if page == "Solver matematic":

    st.title("🧠 AI Math Tutor")
    st.markdown("Platformă pentru rezolvarea exercițiilor matematice")
    st.markdown("---")

    # SIDEBAR EXAMENE
    st.sidebar.markdown("---")
    st.sidebar.title("📚 Subiecte examen")

    bac_links = [
        "https://www.pro-matematica.ro/bacalaureat/2023.php",
        "https://www.pro-matematica.ro/bacalaureat/2022.php",
        "https://www.pro-matematica.ro/bacalaureat/2021.php"
    ]

    class8_links = [
        "https://www.pro-matematica.ro/evaluare-nationala/2023.php",
        "https://www.pro-matematica.ro/evaluare-nationala/2022.php"
    ]

    exam = st.sidebar.selectbox(
        "Alege examenul",
        ["None","Evaluare Națională","BAC"]
    )

    if exam == "BAC":
        if st.sidebar.button("Generează variantă BAC"):
            link = random.choice(bac_links)
            st.sidebar.markdown(f"[Deschide subiect]({link})")

    if exam == "Evaluare Națională":
        if st.sidebar.button("Generează variantă EN"):
            link = random.choice(class8_links)
            st.sidebar.markdown(f"[Deschide subiect]({link})")
    def preprocess_input(text):
        

        text = text.replace(" ", "")
        text = text.replace("π", "pi")

        # -----------------------
        # f(x)=
        # -----------------------
        text = re.sub(r'f\(x\)=', '', text)

        # -----------------------
        # INTEGRALE
        # -----------------------
        match = re.search(r'∫(.+?)dx', text)
        if match:
            expr = match.group(1)
            expr = expr.replace("^", "**")
            return f"integrate({expr})"

        # -----------------------
        # PUTERI
        # -----------------------
        text = text.replace("^", "**")

        # -----------------------
        # MULTIPLICARE (SAFE)
        # -----------------------
        text = re.sub(r'(\d)([a-z])', r'\1*\2', text)

        # ❗ IMPORTANT: NU mai folosim ([a-z])\( pentru că strică sin(...)
        
        # -----------------------
        # TRIG (DOAR dacă NU au paranteze)
        # -----------------------
        # doar dacă NU există deja paranteză
        text = re.sub(r'(sin|cos|tan)(pi/[0-9]+)', r'\1(\2)', text)

        # sinx → sin(x) DOAR dacă nu e deja sin(...)
        text = re.sub(r'(sin|cos|tan)([a-z])(?!\()', r'\1(\2)', text)

        return text
    def fix_parentheses(expr):
        open_count = expr.count("(")
        close_count = expr.count(")")

        if open_count > close_count:
            expr += ")" * (open_count - close_count)

        elif close_count > open_count:
            expr = expr[:-(close_count - open_count)]

        return expr
        # LAYOUT
    col1, col2 = st.columns([2,1])
# ================= LEFT =================
    with col1:

        exercise = st.text_input(
            "✏️ Introdu exercițiul",
            placeholder="ex: x^2 + 2x"
        )

        if st.button("🚀 Rezolvă", use_container_width=True):

            try:
                # 🔥 preprocess o singură dată
                processed_exercise = preprocess_input(exercise)

                response = requests.post(
                    "http://127.0.0.1:8000/solve",
                    json={"exercise": processed_exercise}
                )

                data = response.json()

                # ================= REZULTAT =================
                st.markdown("### 📊 Rezultat")

                try:
                    st.latex(data["result"])
                except:
                    st.write(data["result"])

                # ================= PASI =================
                if "steps" in data:
                    st.markdown("### 📚 Pași rezolvare")
                    for i, step in enumerate(data["steps"], 1):
                        st.write(f"Pasul {i}: {step}")

                # ================= GRAFIC =================
                if processed_exercise and "x" in processed_exercise:

                    st.markdown("---")

                    try:
                        x = sp.symbols('x')

                        # 🔥 ECUAȚIE
                        if "=" in processed_exercise:

                            st.subheader("📈 Grafic ecuație")

                            left, right = processed_exercise.split("=")
                            expr = sp.sympify(left) - sp.sympify(right)

                            f = sp.lambdify(x, expr, "numpy")

                            xs = np.linspace(-10, 10, 400)
                            ys = f(xs)

                            fig = go.Figure()

                            fig.add_trace(go.Scatter(
                                x=xs,
                                y=ys,
                                mode="lines",
                                name="f(x)"
                            ))

                            # axa X
                            fig.add_trace(go.Scatter(
                                x=xs,
                                y=[0]*len(xs),
                                mode="lines",
                                name="y=0",
                                line=dict(dash="dash")
                            ))

                        # 🔥 INTEGRALĂ
                        elif "integrate" in processed_exercise:

                            st.subheader("📈 Grafic integrală")

                            expr_str = processed_exercise.replace("integrate(", "").replace(")", "")
                            expr = sp.sympify(expr_str)

                            integral = sp.integrate(expr, x)

                            f = sp.lambdify(x, integral, "numpy")

                            xs = np.linspace(-10, 10, 400)
                            ys = f(xs)

                            fig = go.Figure()

                            fig.add_trace(go.Scatter(
                                x=xs,
                                y=ys,
                                mode="lines",
                                name="∫f(x)dx"
                            ))

                        # 🔥 FUNCȚIE NORMALĂ
                        else:

                            st.subheader("📈 Grafic funcție")

                            expr = sp.sympify(processed_exercise)

                            f = sp.lambdify(x, expr, "numpy")

                            xs = np.linspace(-10, 10, 400)
                            ys = f(xs)

                            fig = go.Figure()

                            fig.add_trace(go.Scatter(
                                x=xs,
                                y=ys,
                                mode="lines",
                                name="f(x)"
                            ))

                        # 🔥 layout comun
                        fig.update_layout(
                            template="plotly_white",
                            hovermode="x unified"
                        )

                        fig.update_xaxes(showgrid=True)
                        fig.update_yaxes(showgrid=True)

                        st.plotly_chart(fig, width="stretch")

                    except Exception as e:
                        st.error(f"Eroare grafic: {e}")

            except Exception as e:
                st.error(f"Eroare server: {e}")
    # ================= RIGHT =================
    with col2:

        st.subheader("💡 Exemple rapide")

        if st.button("2+3"):
            st.session_state.example = "2+3"

        if st.button("x**2"):
            st.session_state.example = "x**2"

        if st.button("diff(x**2)"):
            st.session_state.example = "diff(x**2)"
    # =========================
    # SISTEME ECUATII
    # =========================

    st.markdown("---")
    st.subheader("🔢 Rezolvă sistem de ecuații")

    eq1 = st.text_input("Ecuația 1 (ex: x + y = 5)")
    eq2 = st.text_input("Ecuația 2 (ex: x - y = 1)")

    if st.button("Rezolvă sistem"):

        try:

            x,y = sp.symbols('x y')

            left1,right1 = eq1.split("=")
            left2,right2 = eq2.split("=")

            eq1_sym = sp.Eq(sp.sympify(left1),sp.sympify(right1))
            eq2_sym = sp.Eq(sp.sympify(left2),sp.sympify(right2))

            solution = sp.solve((eq1_sym,eq2_sym),(x,y))

            st.write("Soluția sistemului:",solution)

        except:

            st.error("Nu pot rezolva sistemul")
            
# =========================
# INIT SESSION STATE
# =========================
if "ocr_text" not in st.session_state:
    st.session_state.ocr_text = ""

if "result" not in st.session_state:
    st.session_state.result = ""

if "steps" not in st.session_state:
    st.session_state.steps = []

# =========================
# FUNCȚII SMART
# =========================
def fix_ocr_errors(text):
    text = text.lower()

    text = text.replace("\n", "")
    text = text.replace(" ", "")

    # -----------------------
    # RADICAL
    # -----------------------
    text = text.replace("√", "sqrt")
    text = text.replace("v", "sqrt")
    text = re.sub(r'sqrt([0-9a-z\-\+\*/]+)', r'sqrt(\1)', text)
    text = re.sub(r'sqrt(\d+)', r'sqrt(\1)', text)
    
    # -----------------------
    # PUTERI (SAFE VERSION)
    # -----------------------

    # DOAR unicode
    text = text.replace("²", "**2")
    text = text.replace("³", "**3")

    # DOAR dacă există ^
    text = text.replace("^", "**")

    # -----------------------
    # MULTIPLICARE
    # -----------------------
    text = re.sub(r'(\d)(x)', r'\1*\2', text)
    text = re.sub(r'(x)(\d)', r'\1*\2', text)

    # -----------------------
    # INTEGRALĂ
    # -----------------------
    text = text.replace("∫", "integrate")

    # -----------------------
    # PI
    # -----------------------
    text = text.replace("π", "pi")

    # -----------------------
    # FRACTII
    # -----------------------
    text = text.replace(":", "/")

    # -----------------------
    # VIRGULĂ
    # -----------------------
    text = text.replace(",", ".")

    return text

def smart_math_parser(text):
    text = fix_ocr_errors(text)

    text = text.replace("−", "-")

    text = re.sub(r'[^0-9a-z+\-*/=().]', '', text)

    if "d/dx" in text:
        expr = text.split("d/dx")[-1]
        return f"diff({expr})"

    if "integrate" in text:
        expr = text.replace("integrate", "")
        expr = expr.replace("dx", "")
        return f"integrate({expr})"

    return text

def clean_text(text):
    text = text.replace("\n", "")
    text = text.replace(" ", "")

    text = re.sub(r'[^0-9a-zA-Z+\-*/=().√²³π]', '', text)

    return text

# =========================
# UI
# =========================
st.markdown("---")
st.subheader("📷 Fotografiază sau încarcă exercițiul")

uploaded_file = st.file_uploader(
    "📁 Încarcă imagine",
    type=["png", "jpg", "jpeg"],
    key="upload_final"
)

img_file = st.camera_input(
    "📷 Fă o poză",
    key="camera_final"
)

image_source = uploaded_file if uploaded_file is not None else img_file

# =========================
# CROP + OCR
# =========================
if image_source is not None:

    image = Image.open(image_source)
    img_np = np.array(image)

    st.image(image, caption="Imagine selectată", width="stretch")

    st.markdown("### ✂️ Selectează zona exercițiului")

    h, w = img_np.shape[:2]

    left = st.slider("⬅️ Stânga", 0, w, 0)
    right = st.slider("➡️ Dreapta", 0, w, w)

    top = st.slider("⬆️ Sus", 0, h, 0)
    bottom = st.slider("⬇️ Jos", 0, h, h)

    left, right = sorted([left, right])
    top, bottom = sorted([top, bottom])

    if right - left > 10 and bottom - top > 10:
        preview = img_np[top:bottom, left:right]
        st.image(preview, caption="Preview selecție", width="stretch")
    else:
        st.warning("Selectează o zonă validă")

# =========================
# OCR (VARIANTA STABILĂ FINALĂ)
# =========================
if st.button("🔍 Procesează exercițiul"):

    if right - left < 10 or bottom - top < 10:
        st.error("Zona prea mică")
    else:

        cropped = img_np[top:bottom, left:right]

        # conversie sigură
        if len(cropped.shape) == 3:
            img = cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR)
        else:
            img = cropped.copy()

        # 🔥 PREPROCESSING MINIM (cheia!)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3,3), 0)

        _, thresh = cv2.threshold(
            gray, 0, 255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        st.image(thresh, caption="Procesată", width="stretch")

        # 🔥 OCR CU WHITELIST ECHILIBRAT
        raw_text = pytesseract.image_to_string(
            thresh,
            config='--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz+-=*/().√^πv'
        )

       # st.write("RAW:", raw_text)

        # 🔥 CURĂȚARE (fără distrugere)
        cleaned = clean_text(raw_text)

        #st.write("✔ Curățat:", cleaned)

        # ⚠️ IMPORTANT: NU parsăm aici
        st.session_state.ocr_text = cleaned
        st.session_state.result = ""
        st.session_state.steps = []
# =========================
# EDITARE + REZOLVARE
# =========================
if st.session_state.ocr_text:

    st.markdown("### ✏️ Modifică exercițiul (dacă e nevoie)")

    user_input = st.text_input(
        "Exercițiu",
        value=st.session_state.ocr_text
    )

    if st.button("🧠 Rezolvă exercițiul"):

        try:
            parsed = smart_math_parser(user_input)

            st.write("📐 Interpretare:", parsed)

            response = requests.post(
                "http://127.0.0.1:8000/solve",
                json={"exercise": parsed}
            )

            data = response.json()

            if "result" in data:
                st.session_state.result = data["result"]
                st.session_state.steps = data.get("steps", [])
            else:
                st.error("Eroare backend")

        except Exception as e:
            st.error("Eroare rezolvare")
            st.caption(str(e))

# =========================
# REZULTAT
# =========================
if st.session_state.result:

    st.subheader("📊 Rezultat")

    try:
        st.latex(st.session_state.result)
    except:
        st.write(st.session_state.result)

    if st.session_state.steps:

        st.markdown("---")
        st.subheader("📚 Pași de rezolvare")

        for i, step in enumerate(st.session_state.steps, 1):
            with st.expander(f"Pasul {i}"):
                st.write(step)
    # EXEMPLE
    # =========================

st.markdown("---")
st.subheader("💡 Exemple")

col1,col2 = st.columns(2)

with col1:
        st.code("2+3")
        st.code("2*x + 5 = 15")
        st.code("diff(x**2)")

with col2:
        st.code("integrate(x**2)")
        st.code("sin(pi/2)")
        st.code("aria cercului raza 5")