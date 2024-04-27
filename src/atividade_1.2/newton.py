def newton(funcao, x0):
    iteracao_maxima = 100
    tolerancia = 1e-05
    
    x=x0
    for iteracao in range (1, iteracao_maxima+1):
        f, df = funcao(x)
        dx = -f/df 
        x += dx
        erro_absoluto = abs(dx) 
        
        print(f"Iteracao {iteracao}: Raiz = {x}, Erro = {erro_absoluto}")    

        if erro_absoluto < tolerancia:  
            return x, iteracao, 0
        
        if iteracao == iteracao_maxima:
            return x, iteracao, 1  
    
def f(x): 
    funcao = x**3 - 2*x + 2
    derivada_funcao = 3*x**2 - 2
    #funcao = x**4 + 2*x**3 - 13*x**2 - 14*x + 24
    #derivada_funcao = 4*x**3 + 6*x**2 - 26*x - 14
    return funcao, derivada_funcao

raiz, iteracoes, erro = newton(f, 0)