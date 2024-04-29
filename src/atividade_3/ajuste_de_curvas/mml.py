import numpy as np

def metodo_minimos_lineares(x, y):
    n = len(x)
    
    somatorio_x = np.sum(x)
    somatorio_y = np.sum(y)
    somatorio_x2 = np.sum(x**2)
    somatorio_xy = np.sum(x*y)
    
    A = np.array([[somatorio_x2, somatorio_x], [somatorio_x, n]])
    B = np.array([somatorio_xy, somatorio_y])
    
    solucao = np.linalg.solve(A, B)
    a = solucao[0]
    b = solucao[1]
    
    return a, b

x = np.array([1.3, 3.4, 5.1, 6.8, 8]) 
y = np.array([2, 5.2, 3.8, 6.1, 5.8])

a, b = metodo_minimos_lineares(x, y)

print("Coeficiente a e':", a)
print("Coeficiente b e':", b)