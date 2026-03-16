import sympy as sp

def solve_fraction(expr):

    result = sp.simplify(expr)

    return {
        "type":"fraction",
        "steps":[
            "Transformăm fracția.",
            "Simplificăm rezultatul."
        ],
        "result": str(result)
    }