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
import cv2 # type: ignore
import tempfile

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

    # LAYOUT
    col1, col2 = st.columns([2,1])

    # ================= LEFT =================
    with col1:

        exercise = st.text_input(
            "✏️ Introdu exercițiul",
            placeholder="ex: x**2 + 2*x"
        )

        if st.button("🚀 Rezolvă", use_container_width=True):

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/solve",
                    json={"exercise": exercise}
                )

                data = response.json()

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
                if exercise and "x" in exercise and "=" not in exercise:

                    st.markdown("---")
                    st.subheader("📈 Grafic funcție")

                    try:
                        x = sp.symbols('x')
                        expr = sp.sympify(exercise)

                        f = sp.lambdify(x, expr, "numpy")

                        xs = np.linspace(-10, 10, 400)
                        ys = f(xs)

                        # FIX IMPORTANT
                        ys = np.array(ys, dtype=float) if isinstance(ys, (list, np.ndarray)) else np.full_like(xs, ys)

                        fig = go.Figure()

                        fig.add_trace(go.Scatter(
                            x=xs,
                            y=ys,
                            mode="lines",
                            name="f(x)"
                        ))

                        fig.update_layout(
                            template="plotly_white",
                            title="Graficul funcției",
                            hovermode="x unified"
                        )

                        fig.update_xaxes(showgrid=True)
                        fig.update_yaxes(showgrid=True)

                        st.plotly_chart(fig, use_container_width=True)

                    except Exception as e:
                        st.error(f"Eroare grafic: {e}")

            except Exception as e:
                st.error(f"Eroare server: {e}")

# ================= RIGHT =================
    with col2:

        st.subheader("💡 Exemple rapide")
        st.code("2+3")
        st.code("x**2")
        st.code("diff(x**2)")
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
    # OCR DIN IMAGINE
    # =========================

    st.markdown("---")
    st.subheader("📸 Rezolvă exercițiu din imagine")
    st.info("📱 Funcționează și pe telefon")

    uploaded_file = st.file_uploader(
        "Încarcă o imagine (poză cu exercițiul)",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        st.image(uploaded_file, caption="Imagine încărcată", use_container_width=True)

        if st.button("📸 Procesează imagine", key="ocr_btn"):

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/solve-image",
                    files={"file": ("image.png", uploaded_file, "image/png")}
                )

                data = response.json()

                st.subheader("📄 Text detectat:")
                st.write(data["detected_text"])

                # trimite direct la solver
                if st.button("Rezolvă automat", key="auto_btn"):

                    response2 = requests.post(
                        "http://127.0.0.1:8000/solve",
                        json={"exercise": data["detected_text"]}
                    )

                    data2 = response2.json()

                    st.subheader("📊 Rezultat")

                    try:
                        st.latex(data2["result"])
                    except:
                        st.write(data2["result"])

            except:
                st.error("Eroare la procesarea imaginii")



st.markdown("---")
st.subheader("📷 Cameră live (poză direct)")

img_file = st.camera_input("Fă o poză")

if img_file is not None:

    image = Image.open(img_file)
    st.image(image, caption="Poză capturată")

    if st.button("🔍 Detectează exercițiu"):

        gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)

        st.subheader("📄 Text detectat:")
        st.code(text)

        if st.button("🧠 Rezolvă automat"):

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/solve",
                    json={"exercise": text}
                )

                data = response.json()

                st.subheader("📊 Rezultat")

                try:
                    st.latex(data["result"])
                except:
                    st.write(data["result"])

            except Exception as e:
                st.error("🚫 Eroare server")
                st.caption(str(e))
    # =========================
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