import sympy as sp

def solve_equation(expr):

    x = sp.symbols('x')

    left, right = expr.split("=")

    equation = sp.Eq(sp.sympify(left), sp.sympify(right))

    solution = sp.solve(equation, x)

    return {
        "type":"equation",
        "steps":[
            "Separăm membrii ecuației.",
            "Mutăm termenii necunoscuți.",
            "Rezolvăm ecuația."
        ],
        "result": str(solution)
    }