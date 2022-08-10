# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:44:49 2017

@author: Wescley
"""
import math as mt

#função em que se deseja encontrar a raiz
def f(x):
    return 3*x**3 + x - 3
    
#funçao para encontrar o ponto fixo. Através de teoremas para determinação do ponto fixo
#pode-se concluir que o ponto fixo está fora do intervalo em que o teorema é válido
#solução para contornar o problema encontra-se abaixo
def g(x):
    return 3 - 3*x**3

#necessário função inversa para resolver o problema. o ponto fixo está fora do intervalo 
#em que a função g(x) converge para o ponto fixo
#agradecimentos: prof lucas ruiz que ajudou a chegar nessa conclusão
def ginv(x):
    return (1 - x/3)**(1/3)
     
#contador para ter noção de quantas iterações foram necessarias
contador = 0        
#entrada do valor inicial para iterações. Necessário estar entre -3 e 3
x0 = float(input("Entre com o valor inicial de teste"))
#aproximação de 10^(-14) = 0 por limites de computação
while ((ginv(x0) - x0 > 1e-14) or (ginv(x0) - x0 < -1e-14)):
    x0 = ginv(x0)
    contador += 1
else:
    print("O da raíz se aproxima de ", x0)
    print("Foram necessárias ", contador, " iterações para chegar ao resultado")
        
