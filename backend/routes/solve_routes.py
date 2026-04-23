from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import sympy as sp
from backend.services.ocr_service import extract_text

router = APIRouter()

class MathProblem(BaseModel):
    exercise: str

# =========================
# SOLVE NORMAL
# =========================
@router.post("/solve")
def solve(problem: MathProblem):

    exercise = problem.exercise.lower()

    try:
        x = sp.symbols('x')

        # =========================
        # 🔥 TRADUCERI INTELIGENTE
        # =========================

        if "aria cercului" in exercise:
            import re
            r = re.findall(r'\d+', exercise)
            if r:
                r = int(r[0])
                result = sp.pi * r**2
                return {
                    "result": str(result),
                    "steps": [f"Aria cercului: π * r² = π * {r}²"]
                }

        if "derivata" in exercise or "diff" in exercise:
            expr = exercise.replace("derivata", "").strip()
            expr = sp.sympify(expr)
            result = sp.diff(expr, x)
            return {"result": str(result), "steps": ["Derivare efectuată"]}

        # =========================
        # DERIVATA
        # =========================
        if "diff" in exercise or "derivata" in exercise:

            expr_str = exercise.replace("diff", "").replace("derivata", "").strip()
            expr = sp.sympify(expr_str)

            derivative = sp.diff(expr, x)

            steps = [
                f"Funcția este: f(x) = {expr}",
                "Aplicăm regula derivării",
                f"Derivata este: {derivative}"
            ]

            return {
                "result": str(derivative),
                "steps": steps
            }

        # =========================
        # ECUAȚII
        # =========================
        if "=" in exercise:

            left, right = exercise.split("=")
            eq = sp.Eq(sp.sympify(left), sp.sympify(right))
            sol = sp.solve(eq, x)

            steps = [
                f"Ecuația este: {exercise}",
                "Mutăm termenii",
                "Rezolvăm ecuația",
                f"Soluția este: {sol}"
            ]

            return {
                "result": str(sol),
                "steps": steps
            }

        # =========================
        # CALCUL SIMPLU
        # =========================
        expr = sp.sympify(exercise)
        result = expr.evalf()

        steps = [
            f"Calculăm expresia: {exercise}",
            f"Rezultatul este: {result}"
        ]

        return {
            "result": str(result),
            "steps": steps
        }

    except Exception as e:
        return {
            "result": "Eroare",
            "steps": [str(e)]
        }
# =========================
# OCR + SOLVE
# =========================
@router.post("/solve-image")
def solve_image(file: UploadFile = File(...)):

    text = extract_text(file.file)

    try:
        expr = sp.sympify(text)
        result = expr.evalf()

        return {
            "detected_text": str(text),
            "result": str(result)
        }

    except Exception as e:
        return {
            "detected_text": str(text),
            "result": "Nu am putut interpreta",
            "error": str(e)
        }