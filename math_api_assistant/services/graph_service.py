import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def generate_graph(expr):

    x = sp.symbols('x')

    f = sp.sympify(expr)

    func = sp.lambdify(x,f,"numpy")

    xs = np.linspace(-10,10,100)

    ys = func(xs)

    return xs, ys