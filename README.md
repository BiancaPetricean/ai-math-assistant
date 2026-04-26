# 🧠 AI Math Assistant

AI Math Assistant este o aplicație pentru rezolvarea automată a exercițiilor matematice. Utilizatorul poate introduce exerciții manual sau prin imagine, iar aplicația procesează datele și afișează rezultatul împreună cu pașii de rezolvare.

Proiectul este realizat în Python și este organizat modular, separând clar interfața, backend-ul și logica matematică.

---

## 🚀 Funcționalități

Aplicația poate rezolva:

* ✔ expresii matematice simple
* ✔ ecuații algebrice
* ✔ derivate
* ✔ integrale
* ✔ funcții matematice (analiză și grafic)
* ✔ exerciții extrase din imagini (OCR)

Rezultatele sunt afișate împreună cu explicații și pași intermediari.

---

## ⚙️ Tehnologii utilizate

* **Python** – limbaj principal
* **FastAPI** – backend și API
* **Streamlit** – interfața utilizator
* **SymPy** – procesare matematică simbolică
* **OpenCV & Tesseract OCR** – procesare imagine și recunoaștere text
* **Plotly** – vizualizare grafică
* **Git & GitHub** – versionare și colaborare

---

## 📁 Structura proiectului

```
ai-math-assistant/
├── backend/        # API și logică server
│   └── routes/     # rute aplicație
├── frontend/       # interfața Streamlit
├── math_engine/    # logica matematică
├── services/       # servicii auxiliare (OCR etc.)
├── utils/          # funcții ajutătoare
├── database/       # componente pentru date
├── requirements.txt
└── README.md
```

---

## 🧩 Descrierea componentelor

* **backend** – gestionează cererile și logica API
* **frontend** – interfața utilizatorului
* **math_engine** – rezolvarea exercițiilor matematice
* **services** – servicii auxiliare (ex: OCR)
* **utils** – funcții ajutătoare
* **database** – gestionarea datelor (dacă este cazul)

---

## 🛠️ Instalare

Clonați repository-ul:

```
git clone https://github.com/BiancaPetricean/ai-math-assistant.git
```

Intrați în folder:

```
cd ai-math-assistant
```

Creați un mediu virtual:

```
python -m venv venv
```

Activați mediul virtual:

**Windows:**

```
venv\Scripts\activate
```

Instalați dependențele:

```
pip install -r requirements.txt
```

---

## ▶️ Rulare

Porniți backend-ul:

```
uvicorn backend.main:app --reload
```

Porniți interfața:

```
streamlit run frontend/app.py
```

Aplicația va fi disponibilă în browser.

---

## 🧪 Exemple de exerciții

**Expresie:**

```
sqrt(16)
```

**Ecuație:**

```
x^2 = 4
```

**Derivată:**

```
diff(x^2 + 3*x)
```

**Integrală:**

```
∫ x^2 dx
```

**Trigonometrie:**

```
sin(pi/2)
```

---

## 🔄 Workflow Git

Proiectul a fost dezvoltat folosind Git și GitHub, cu workflow pe branch-uri:

* `main` – versiunea stabilă
* `feature-backend` – dezvoltare backend
* `feature-frontend` – dezvoltare interfață
* `feature-ai` – logică AI / matematică

Integrarea modificărilor s-a realizat prin Pull Request-uri.

---

## 📌 Observații

* Aplicația suportă input flexibil (manual + OCR)
* Sunt implementate mecanisme de corectare a input-ului (preprocesare)
* Rezultatele sunt afișate atât simbolic, cât și numeric

---

## 👩‍💻 Autor

Proiect realizat în cadrul unui proiect de echipă (Master).

---