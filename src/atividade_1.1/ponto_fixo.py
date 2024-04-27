import math 

def f(x): 
    return x**2 - x - 2

def g(x):
    return (2 + x)**(1/2)

x0 = 2.5
tolerancia = 0.001
nmax = 15  
i = 0 

print('i |   x ')
print(f'{i} | {x0:.3f}')

while i < nmax:
    x = g(x0)
    erro_a = abs(x-x0)
    i += 1
    print(f'{i} | {x:.3f}')
    x0 = x
    if erro_a < tolerancia:
        break