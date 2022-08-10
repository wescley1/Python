# -*- coding: utf-8 -*-
# Suponha que a posição de um ponto no espaço bidimensional é dado em coordenadas polares $r$, $\theta$ e queremos convertê-lo em coordenadas cartesianas x , y. Escreva um programa para fazer essa conversão. Para isso faça:
#1 - Obter do usuário os valores de $r$ e $\theta$.
#2 - converter esses valores em coordenadas cartesianas usando as fórmulas:
# $x = rcos(\theta)$ e $y = rsin(\theta)$
from math import cos, sin

r = float(input("entre com o valor do raio:"))
theta = float(input("entre com o valor do angulo(em radianos):"))

x = r*cos(theta)
y = r*sin(theta)

print ("As coordenada no plano cartesiano será:[",x,',',y,"]")


