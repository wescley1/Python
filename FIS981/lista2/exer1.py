# -*- coding: utf-8 -*-
"""

"""
#entrada de dados
import math as mt

l1 = float(input("Entre com a distancia do planeta no periélio em metros "))
v1 = float(input("Entre vom a velocidade do planeto no periélio em metros por segundo "))

#definindo as constantes

G = 6.6738e-11
M = 1.9891e30

#aplicando a fórmula de bhaskara para resolver a equação quadrática fornecida

v2 = (2*G*M/(v1*l1) - mt.sqrt( (2*G*M/(v1*l1))**2 + 4*(v1**2 - 2*G*M/l1) ))/2

#realizando os calculos requisitados no exercicio
l2 = l1*v1/v2
a = (l1 + l2)/2
b = mt.sqrt(l1*l2)
#aqui utiliza-se a funçao math.pi que retorna o valor da constante pi
T = 2*mt.pi*a*b/(l1*v1)
e = (l2 - l1)/(l2 + l1)

#arredondando 
l2 = round(l2, 2)
a = round (a, 2)
b = round(b,2)
T = round(T, 2)
e = round(e, 2)
v2 = round (v2, 2)


print("O período do corpo será", T, "segundos")
print("O raio maior da orbita será", l2, "metros" )
print("A velocidade do corpo no afélio será", v2, "m/s")
print("A excentricidade da órbita é", e)

