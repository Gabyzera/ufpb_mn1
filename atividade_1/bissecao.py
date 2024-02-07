import math 

def f(x): 
    return 2*x**3 - math.cos(x+1) - 3

a, b = - 1, 2 
x = (a+b)/2
tolerancia = 0.001
nmax = 15
i = 0

print('i |   a   |  f(a)  |   b   | f(b) |   x   |  f(x)')
print(f'{0} |{a:.3f} | {f(a):.3f} | {b:.3f} |{f(b):.3f}| {x:.3f} | {f(x):.3f}')

if f(a)*f(b) < 0:
    while i < nmax: 
        x = (a+b)/2
        erro_r = abs((b-a)/x)
        i += 1
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x 
        print(f'{i} | {a:.3f} | {f(a):.3f} | {b:.3f} |{f(b):.3f}| {x:.3f} | {f(x):.3f}')
        if erro_r < tolerancia:
            break