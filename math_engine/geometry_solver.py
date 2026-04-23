import math

def solve_geometry(expr):

    expr = expr.lower()

    if "aria cercului" in expr:

        r = int(expr.split()[-1])

        area = math.pi * r**2

        return {
            "type":"geometry",
            "steps":[
                "Formula ariei cercului.",
                "A = π * r²"
            ],
            "result": str(area)
        }

    if "perimetrul patratului" in expr:

        l = int(expr.split()[-1])

        p = 4 * l

        return {
            "type":"geometry",
            "steps":[
                "Perimetrul pătratului = 4 * latura"
            ],
            "result": str(p)
        }