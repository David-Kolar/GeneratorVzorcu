import sympy
from math import comb

def make_formula(n):
    formulas = [sympy.sympify("(q**(x+1) - 1)/(q - 1)")]
    q = sympy.sympify("q")
    for i in range(1, n+1):
        formula = sympy.sympify(f"(x+1)**{i}*q**(x+1)")
        for j in range(1, i+1):
            formula -= comb(i, j)*formulas[i - j]*q
        formulas.append(formula/sympy.sympify("q - 1"))
    return formulas[n]

def test_formula(formula, n, q):
    s = 0
    for i in range(20):
        s += i**n*q**i
        print(s, formula.subs("x", i))
for i in range(4):
    f = sympy.simplify(make_formula(i))
    print(sympy.factor(f))

