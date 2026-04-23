import sympy as sp

def solve_derivative(expr):

    x = sp.symbols('x')

    f = sp.sympify(expr.replace("diff",""))

    result = sp.diff(f,x)

    return {
        "type":"derivative",
        "steps":[
            "Aplicăm regulile de derivare."
        ],
        "result": str(result)
    }


def solve_integral(expr):

    x = sp.symbols('x')

    f = sp.sympify(expr.replace("integrate",""))

    result = sp.integrate(f,x)

    return {
        "type":"integral",
        "steps":[
            "Aplicăm regulile de integrare."
        ],
        "result": str(result)
    }