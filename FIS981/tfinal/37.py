# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:05:06 2016

Mandelbrot Set from -2 to 2 Re x Im
author: Wescley de Carvalho Dimas
matricula: 2016006635

obs.:
    devido a quantidade de iteraçoes e numeros para serem avaliados o programa leva
    um bom tempo para ser executado
"""
#primeiro está definida a seçao de imports 

import numpy as np
import matplotlib.pyplot as plt

#funçao para definir se o numero está contido dentro do conjunto de mandelbrot ou nao
def mandelbrot(z,a,b):
    c = complex(a,b)
    for n in range(100):
        if (abs(z) >= 2):
            return 0
        z = z**2 + c
    return 1
    
#serao definidos dois vetores de -2 a 2 com os numeros para serem avaliados
#se fazem parte ou nao do conjunto e duas listas vazias que contem os numeros do conjunto

"""
para que o programa execute mais rapido, reduzir o valor da variável qtd definida abaixo
"""
qtd = 5000
re = np.linspace(-2.0,2.0,qtd)
im = np.linspace(-2.0,2.0,qtd)
x = []
y = []

#através dos dois laços de for é possível passar por todos os pontos definidos e, entao,
#avaliar se estao no conjunto ou nao (utilizando a funcao definida acima)
for n in range(re.__len__()):
    for m in range(im.__len__()):
        if ( mandelbrot(0,re[n],im[m]) ):
            x.append(re[n])
            y.append(im[m])
            

#depois das listas x e y preenchidas é possivel criar o scatter dos numeros e assim 
#formar a imagem completa do conjunto            
plt.scatter(x,y,color='black',s=1)

plt.xlim(min(x)-0.05,max(x)+0.05)
plt.ylim(min(y)-0.05,max(y)+0.05)
plt.xlabel("Re")
plt.ylabel("Im")

plt.show()
        



