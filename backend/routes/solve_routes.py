
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import sympy as sp
from backend.services.ocr_service import extract_text


router = APIRouter()

class MathProblem(BaseModel):
    exercise: str


# =========================
# SOLVE NORMAL (FINAL)
# =========================
@router.post("/solve")
def solve(problem: MathProblem):

    exercise = problem.exercise.lower()

    try:
        x = sp.symbols('x')

        # 🔥 mapping global (IMPORTANT)
        local_dict = {
            "sin": sp.sin,
            "cos": sp.cos,
            "tan": sp.tan,
            "pi": sp.pi,
            "sqrt": sp.sqrt
        }

        # =========================
        # ARIA CERCULUI
        # =========================
        if "aria cercului" in exercise:
            import re
            r = re.findall(r'\d+', exercise)
            if r:
                r = int(r[0])
                result = sp.pi * r**2
                return {
                    "result": str(result),
                    "steps": [
                        "Formula: A = π * r²",
                        f"A = π * {r}²",
                        f"A = {result}"
                    ]
                }

        # =========================
        # DERIVATA
        # =========================
        if "derivata" in exercise or "diff" in exercise:

            expr_str = exercise.replace("diff", "").replace("derivata", "").strip()
            expr = sp.sympify(expr_str, locals=local_dict)

            derivative = sp.diff(expr, x)

            return {
                "result": str(derivative),
                "steps": [
                    f"f(x) = {expr}",
                    "Derivăm funcția",
                    f"f'(x) = {derivative}"
                ]
            }

        # =========================
        # ECUAȚII
        # =========================
        if "=" in exercise:

            left, right = exercise.split("=")

            left_expr = sp.sympify(left, locals=local_dict)
            right_expr = sp.sympify(right, locals=local_dict)

            steps = [f"Ecuatia: {left_expr} = {right_expr}"]

            eq = sp.Eq(left_expr, right_expr)

            simplified = sp.simplify(eq.lhs - eq.rhs)

            steps.append("Aducem totul în stânga")
            steps.append(f"{simplified} = 0")

            sol = sp.solve(simplified, x)

            steps.append("Rezolvăm ecuația")
            steps.append(f"Soluția: {sol}")

            return {
                "result": str(sol),
                "steps": steps
            }
        # =========================
        # FUNCȚII (ANALIZĂ REALĂ)
        # =========================
        if "x" in exercise:

            expr = sp.sympify(exercise, locals=local_dict)

            steps = []
            steps.append(f"Funcția este: f(x) = {expr}")

            # simplificare
            simplified = sp.simplify(expr)
            steps.append(f"Simplificăm: {simplified}")

            # factorizare (doar dacă e diferită)
            factored = sp.factor(expr)
            if factored != expr:
                steps.append(f"Factorizăm: {factored}")

            # derivata
            derivative = sp.diff(expr, x)
            steps.append(f"Derivata: f'(x) = {derivative}")

            return {
                "result": str(simplified),
                "steps": steps
            }


        # =========================
        # CALCUL SIMPLU
        # =========================
        expr = sp.sympify(exercise, locals=local_dict)
        result = sp.simplify(expr)

        return {
            "result": str(result),
            "steps": [
                f"Calculăm expresia: {expr}",
                f"Rezultat: {result}"
            ]
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

    import re

    text = extract_text(file.file)

    try:
        cleaned = text.lower()

        cleaned = cleaned.replace("^", "**")
        cleaned = cleaned.replace("−", "-")
        cleaned = cleaned.replace(" ", "")

        cleaned = cleaned.replace("x²", "x**2")
        cleaned = cleaned.replace("x³", "x**3")

        cleaned = re.sub(r'(\d)(x)', r'\1*\2', cleaned)
        cleaned = re.sub(r'[^0-9xX+\-*/=().]', '', cleaned)

        x = sp.symbols('x')

        if "=" in cleaned:
            left, right = cleaned.split("=")
            eq = sp.Eq(sp.sympify(left), sp.sympify(right))
            result = sp.solve(eq, x)
        else:
            expr = sp.sympify(cleaned)
            result = expr.evalf()

        return {
            "detected_text": text,
            "cleaned_text": cleaned,
            "result": str(result)
        }

    except Exception as e:
        return {
            "detected_text": text,
            "cleaned_text": cleaned,
            "result": "Nu am putut interpreta",
            "error": str(e)
        }

