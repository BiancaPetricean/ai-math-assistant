import random

def generate_equation():

    a = random.randint(1,10)
    b = random.randint(1,10)
    x = random.randint(1,10)

    c = a*x + b

    return f"{a}*x + {b} = {c}"