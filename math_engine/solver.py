import sympy as sp
import math
import re

x = sp.symbols('x')

# ==============================
# UTILITARE
# ==============================

def clean_expression(expr):

    expr = expr.replace("^", "**")
    expr = expr.strip()

    return expr


# ==============================
# DETECTARE TIP EXERCITIU
# ==============================

def detect_problem(expr):

    expr = expr.lower()

    if "aria" in expr or "perimetr" in expr:
        return "geometry"

    if "diff(" in expr:
        return "derivative"

    if "integrate(" in expr:
        return "integral"

    if "limit" in expr:
        return "limit"

    if "sin" in expr or "cos" in expr or "tan" in expr:
        return "trigonometry"

    if "=" in expr:
        return "equation"

    if "x" in expr:
        return "function"

    return "arithmetic"


# ==============================
# ARITMETICA
# ==============================

def solve_arithmetic(expr):

    result = sp.sympify(expr)

    return {
        "type": "arithmetic",
        "steps":[
            {
                "text":"Scriem expresia matematică",
                "math":sp.latex(sp.sympify(expr))
            },
            {
                "text":"Calculăm rezultatul expresiei",
                "math":sp.latex(result)
            }
        ],
        "result":str(result)
    }


# ==============================
# ECUATII
# ==============================

def solve_equation(expr):

    left,right = expr.split("=")

    left_expr = sp.sympify(left)
    right_expr = sp.sympify(right)

    equation = sp.Eq(left_expr,right_expr)

    solution = sp.solve(equation,x)

    return {

        "type":"equation",

        "steps":[

            {
                "text":"Scriem ecuația inițială",
                "math":f"{sp.latex(left_expr)} = {sp.latex(right_expr)}"
            },

            {
                "text":"Mutăm termenii pentru a izola necunoscuta",
                "math":sp.latex(left_expr-right_expr)+" = 0"
            },

            {
                "text":"Rezolvăm ecuația",
                "math":f"x = {sp.latex(solution[0])}"
            }

        ],

        "result":str(solution)

    }


# ==============================
# DERIVATE
# ==============================

def solve_derivative(expr):

    expr = expr.replace("diff","")

    f = sp.sympify(expr)

    derivative = sp.diff(f,x)

    return{

        "type":"derivative",

        "steps":[

            {
                "text":"Funcția dată",
                "math":"f(x) = "+sp.latex(f)
            },

            {
                "text":"Aplicăm regulile de derivare",
                "math":"f'(x) = "+sp.latex(derivative)
            }

        ],

        "result":str(derivative)

    }


# ==============================
# INTEGRALE
# ==============================

def solve_integral(expr):

    expr = expr.replace("integrate","")

    f = sp.sympify(expr)

    integral = sp.integrate(f,x)

    return{

        "type":"integral",

        "steps":[

            {
                "text":"Scriem integrala",
                "math":"\\int "+sp.latex(f)+" dx"
            },

            {
                "text":"Calculăm integrala",
                "math":sp.latex(integral)
            }

        ],

        "result":str(integral)

    }


# ==============================
# LIMITE
# ==============================

def solve_limit(expr):

    expr = expr.replace("limit","")

    f = sp.sympify(expr)

    limit_value = sp.limit(f,x,0)

    return{

        "type":"limit",

        "steps":[

            {
                "text":"Funcția analizată",
                "math":sp.latex(f)
            },

            {
                "text":"Calculăm limita când x → 0",
                "math":sp.latex(limit_value)
            }

        ],

        "result":str(limit_value)

    }


# ==============================
# TRIGONOMETRIE
# ==============================

def solve_trigonometry(expr):

    result = sp.sympify(expr)

    return{

        "type":"trigonometry",

        "steps":[

            {
                "text":"Evaluăm expresia trigonometrică",
                "math":sp.latex(sp.sympify(expr))
            },

            {
                "text":"Rezultatul calculului",
                "math":sp.latex(result)
            }

        ],

        "result":str(result)

    }


# ==============================
# ANALIZA FUNCTIILOR
# ============================s

def analyze_function(expr):

    f = sp.sympify(expr)

    derivative = sp.diff(f,x)

    critical_points = sp.solve(derivative,x)

    return{

        "type":"function_analysis",

        "steps":[

            {
                "text":"Funcția analizată",
                "math":"f(x) = "+sp.latex(f)
            },

            {
                "text":"Calculăm derivata",
                "math":"f'(x) = "+sp.latex(derivative)
            },

            {
                "text":"Determinăm punctele critice",
                "math":"x = "+sp.latex(critical_points)
            }

        ],

        "result":str(derivative)

    }


# ==============================
# GEOMETRIE
# ==============================

def solve_geometry(expr):

    expr = expr.lower()

    if "aria cercului" in expr:

        r = float(expr.split()[-1])

        area = math.pi*r**2

        return{

            "type":"geometry",

            "steps":[

                {
                    "text":"Formula ariei cercului",
                    "math":"A = \\pi r^2"
                },

                {
                    "text":"Înlocuim raza",
                    "math":f"A = \\pi \\cdot {r}^2"
                },

                {
                    "text":"Calculăm aria",
                    "math":sp.latex(area)
                }

            ],

            "result":str(area)

        }


    return{

        "type":"geometry",
        "result":"Tip necunoscut"

    }


# ==============================
# SOLVER PRINCIPAL
# ==============================

def solve_problem(expr):

    expr = clean_expression(expr)

    problem_type = detect_problem(expr)

    try:

        if problem_type=="arithmetic":
            return solve_arithmetic(expr)

        if problem_type=="equation":
            return solve_equation(expr)

        if problem_type=="derivative":
            return solve_derivative(expr)

        if problem_type=="integral":
            return solve_integral(expr)

        if problem_type=="limit":
            return solve_limit(expr)

        if problem_type=="trigonometry":
            return solve_trigonometry(expr)

        if problem_type=="geometry":
            return solve_geometry(expr)

        if problem_type=="function":
            return analyze_function(expr)

        return{"error":"Tip necunoscut"}

    except Exception as e:

        return{
            "error":"Nu am putut rezolva exercițiul",
            "details":str(e)
        }