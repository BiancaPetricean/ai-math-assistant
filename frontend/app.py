import streamlit as st
import requests
import sympy as sp
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import random
import pandas as pd

# configurare pagină
st.set_page_config(
    page_title="AI Math Tutor",
    page_icon="🧠",
    layout="wide"
)

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

    st.plotly_chart(fig2,use_container_width=True)

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

    # LINKURI EXAMEN

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

    # INPUT

    exercise = st.text_input("✏️ Introdu exercițiul matematic")

    if st.button("Rezolvă exercițiu"):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/solve",
                json={"exercise": exercise}
            )

            data = response.json()

            st.subheader("📊 Rezultat")

            try:
                st.latex(data["result"])
            except:
                st.write(data["result"])

            if "steps" in data:

                st.subheader("📚 Pași rezolvare")

                for step in data["steps"]:

                    if isinstance(step,dict):

                        st.write(step["text"])
                        st.latex(step["math"])

                    else:
                        st.write(step)

            # ANALIZA FUNCTIE

            if "x" in exercise and "=" not in exercise:

                st.markdown("---")
                st.subheader("📈 Analiza funcției")

                x = sp.symbols('x')
                expr = sp.sympify(exercise)

                derivative = sp.diff(expr,x)

                st.write("Derivata:")
                st.latex(sp.latex(derivative))

                critical_points = sp.solve(derivative,x)
                roots = sp.solve(expr,x)

                st.write("Puncte critice:",critical_points)
                st.write("Intersecții Ox:",roots)

                f = sp.lambdify(x,expr,"numpy")

                xs = np.linspace(-10,10,400)
                ys = f(xs)

                fig = go.Figure()

                fig.add_trace(go.Scatter(
                    x=xs,
                    y=ys,
                    mode="lines",
                    line=dict(width=3),
                    name="f(x)"
                ))

                for r in roots:
                    fig.add_trace(go.Scatter(
                        x=[r],
                        y=[0],
                        mode="markers",
                        marker=dict(size=10,color="green"),
                        name="rădăcină"
                    ))

                fig.update_layout(
                    template="plotly_white",
                    title="Graficul funcției"
                )

                st.plotly_chart(fig,use_container_width=True)

        except Exception as e:

            st.error("Nu se poate conecta la server")

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

    # EXEMPLE

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