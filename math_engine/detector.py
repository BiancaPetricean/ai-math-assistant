def detect_problem(expr):
    
    expr = expr.lower()

    if "aria" in expr or "perimetr" in expr:
        return "geometry"

    if "/" in expr:
        return "fraction"

    if "=" in expr:
        return "equation"

    if "diff" in expr:
        return "derivative"

    if "integrate" in expr:
        return "integral"

    if "x" in expr:
        return "function"

    return "arithmetic"