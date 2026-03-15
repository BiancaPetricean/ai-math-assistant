import sympy as sp

def solve_arithmetic(expr):

    result = sp.sympify(expr)

    return {
        "type": "arithmetic",
        "steps": [
            "Calculăm expresia matematică."
        ],
        "result": str(result)
    }