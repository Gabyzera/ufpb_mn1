# 🧮 Atividades de Métodos Numéricos I

## ✍🏼 Descrição
Este repositório contém implementações em Python de métodos numéricos fundamentais para encontrar raízes de funções matemáticas. Sendo alimentado conforme o prosseguimento da matéria de Métodos Numéricos I ministrado na Universidade Federal da Paraíba. 

## 🗒️ Métodos do Projeto
**Método da Bisseção** 

`bissecao.py`: Ele é aplicado a funções contínuas em um intervalo [a,b] onde a função muda de sinal (ou seja, f(a)*f(b) < 0). O método divide iterativamente o intervalo pela metade e seleciona o subintervalo onde a função continua mudando de sinal, convergindo gradualmente para a raiz.

**Método do Ponto Fixo**

`ponto_fixo.py`: Técnica iterativa que converte o problema de encontrar uma raiz de f(x) = 0 em encontrar um ponto fixo de g(x) = x, onde g(x) é uma função derivada de f(x). Requer a escolha de uma função g(x) apropriada e uma estimativa inicial x0.

**Método de Newton**

`newton.py`: Técnica que usa uma abordagem iterativa que começa com uma estimativa inicial e refina essa estimativa usando a tangente da função no ponto de interesse. A cada iteração, a fórmula *xn+1 = xn - f(xn) / df(xn)* é aplicada. O processo é repetido até que o erro absoluto seja menor do que a tolerância, demonstrando que o algoritmo achou uma raiz próxima da desejada ou o número máximo de iterações seja alcancado, indicando que não foi encontrado uma raiz.

**Método Simpson 1/3**

`simpson_um_terco`: Técnica para aproximar o valor de integrais definidas, dividindo a área sob a curva em segmentos de parábolas que passam por três pontos consecutivos, proporcionando maior precisão que a regra dos trapézios.

**Ajuste de curvas**

- `mml.py`: O método busca uma linha reta que minimize os resíduos quadráticos, determinando os coeficientes lineares através de equações normais derivadas das condições de minimização aplicadas aos dados lineares.

- `mmq.py`: O método consiste em encontrar a função (geralmente um polinômio) que melhor se ajusta a um conjunto de dados, minimizando a soma dos quadrados das diferenças entre os valores observados e os valores ajustados pela função. 

## ⚙️ Como executar
Para executar cada script, é necessário ter Python instalado em seu sistema. Ambos os scripts podem ser executados a partir da linha de comando ou através de um ambiente de desenvolvimento que suporte Python.