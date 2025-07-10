from sympy import Derivative, factorial, symbols, sympify
from matplotlib.pyplot import plot, show


x = symbols('x')
f = input('f(x) = ')
y = sympify(input('x = '))
r = sympify(input('r = '))
N = sympify(input('N = '))
i = 1
sty = [sympify(f).subs({x: 0})]
sigma = []
gty = []
while i < N:
    fak = factorial(i)
    df = Derivative(f, x).doit()
    sty.append((df.subs({x: 0}) * x ** i) / fak)
    sigma.append(sum(sty))
    gty.append(sigma[i-1].subs({x: z for z in range(-r, r+1)}))
    f = df
    i = i + 1
print(round(gty[-1], 11))
plot(gty, marker='*', color='red', linestyle=':', alpha=0.5)
show()