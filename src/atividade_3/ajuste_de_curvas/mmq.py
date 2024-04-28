import numpy as np
import matplotlib.pyplot as plt

def metodo_minimos_quadrados(x, y):
    n = len(x)
    
    somatorio_x = np.sum(x)
    somatorio_y = np.sum(y)
    somatorio_x2 = np.sum(x**2)
    somatorio_x3 = np.sum(x**3)
    somatorio_x4 = np.sum(x**4)
    somatorio_x2 = np.sum(x**2)
    somatorio_xy = np.sum(x*y)
    somatorio_x2y = np.sum(x**2 * y)
    
    A = np.array([
        [somatorio_x4, somatorio_x3, somatorio_x2], 
        [somatorio_x3,somatorio_x2, somatorio_x],
        [somatorio_x2, somatorio_x, n]
    ])
    B = np.array([somatorio_x2y, somatorio_xy, somatorio_y])
    
    solucao = np.linalg.solve(A, B)
    a = solucao[0]
    b = solucao[1]
    c = solucao[2]
    
    return a, b, c

x = np.array([0, 1, 2, 3, 4, 5]) 
y = np.array([1, 2, 9, 28, 65, 126])

a, b, c = metodo_minimos_quadrados(x, y)

print(f"Coeficiente a e':{a}")
print(f"Coeficiente b e':{b}")
print(f"Coeficiente c e':{c}")

# criação do gráfico
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', label='Dados Originais') 
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a*x_fit**2 + b*x_fit + c
plt.plot(x_fit, y_fit, 'b-', label=f'Curva de Ajuste: y = {a:.2f}x² + {b:.2f}x + {c:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ajuste Quadrático por Mínimos Quadrados')
plt.legend()
plt.grid(True)
plt.show()