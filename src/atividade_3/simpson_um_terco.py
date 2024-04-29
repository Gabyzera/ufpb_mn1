import numpy as np

def simpson_um_terco(funcao, a, b, n):
    if n % 2 != 0:
        n += 1 
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = funcao(x)
     
    resultado = (h/3)*(y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])
    return resultado

def funcao(x):
    return 1 / (1 + x**2)

resultado = simpson_um_terco(funcao, 0, 1, 6)
print(f'O resultado encontrado foi: {resultado}')