# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 03:00:00 2017

@author: Wescley
"""

#definição da função para encontrar as raízes
def f(x):
    return 3*x**3 + x - 3
    
#função para calcular a bissecção 
def bissec(a,b):
    c = (a + b)/2
    if (f(a)*f(c) <= 0):
        return a, c
    else:
        return c,b
    
#entrada de dados iniciais    
inf = input("Entre com o limite inferior inicial")
sup = input("Entre com o limite superior inicial")

x0 = inf
#contador para verificar quantas iterações foram necessárias
contador = 0
#definindo a aproximação como 1*10^(-14) = 0 devido ao limite computacional
while((f(x0) < -1e-14) or (f(x0) > 1e-14)):
    #estrutura de repetição pra testar os valores da função até encontrar a primeira raíz real
    inf , sup = bissec(inf,sup )
    x0 = inf
    #incremento do contador para saber quantas iterações foram necessárias no final da operação
    contador +=1
else:     
    print("A raiz da função está proxima de", x0)    
    print("Foram necessárias", contador," iterações para chegar ao resultado")
    