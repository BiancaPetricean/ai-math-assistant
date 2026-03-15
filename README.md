# AI Math Assistant

AI Math Assistant este o aplicație pentru rezolvarea exercițiilor matematice. Utilizatorul introduce exercițiul în interfață, iar aplicația îl procesează și afișează rezultatul împreună cu pașii de rezolvare.

Proiectul este realizat în Python și este organizat modular, astfel încât componentele pentru interfață, backend și logica matematică să fie separate.

## Funcționalități

Aplicația poate rezolva exerciții matematice precum:
- expresii matematice simple
- ecuații
- derivate
- integrale

Rezultatul este afișat împreună cu explicații și pași intermediari.

## Tehnologii utilizate

- **Python** – limbajul principal al aplicației
- **FastAPI** – pentru backend și API
- **Streamlit** – pentru interfața utilizatorului
- **SymPy** – pentru procesarea matematică
- **Git și GitHub** – pentru versionare și colaborare în echipă

## Structura proiectului
ai-math-assistant
├── backend
│   └── routes
├── database
├── frontend
├── math_engine
├── services
├── utils
├── requirements.txt
└── README.md
##Descrierea componentelor
backend – gestionează cererile aplicației și logica API
backend/routes – conține rutele aplicației
database – conține componentele legate de gestionarea datelor
frontend – interfața utilizator
math_engine – logica principală pentru rezolvarea exercițiilor matematice
services – servicii auxiliare utilizate în aplicație
utils – funcții ajutătoare

##Instalare
Clonați repository-ul:
git clone https://github.com/BiancaPetricean/ai-math-assistant.git
Intrați în folderul proiectului:
cd ai-math-assistant
Creați un mediu virtual:
python -m venv venv
Activați mediul virtual:
Windows
venv\Scripts\activate
Instalați dependențele:
pip install -r requirements.txt
Rulare
Pornirea backend-ului:
uvicorn backend.main:app --reload
Pornirea interfeței:
streamlit run frontend/app.py
După pornire, aplicația poate fi accesată din browser.

##Exemple de exerciții
Expresie
√(16)
Ecuație
x^2=4
Derivată
d/dx(x^2+3*x)
Integrală
∫(x^2)dx

##Gestionarea proiectului
Proiectul este gestionat folosind Git și GitHub. Pentru dezvoltare a fost folosit un workflow bazat pe branch-uri:
main – versiunea stabilă
dev – integrarea modificărilor
feature-* – dezvoltarea funcționalităților separate
Integrarea codului se face prin Pull Request-uri.

