# -*- coding: utf-8 -*-

#Faça um programa para calcular a sequencia de Fibonacci até 1000.

#variável para controle
flag = True

#váriveis com os números da sequência
x1 = 1
x2 = 1
#exibe os dois primeiros números já definidos
print (x1)
print (x2)

#contador dos termos
index = 2

#função para limitar os 1000 termos
while (index < 1000):
    print (x1 + x2)
    #if para saber qual das variáveis ser incrementada
    if flag:
        x1 = x1 + x2
    else:
        x2 = x1 + x2
    #controlador para alternar entre as varáveis alternáveis
    flag = not(flag)
    index+=1

