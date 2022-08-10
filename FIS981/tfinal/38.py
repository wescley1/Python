# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:15:16 2016

Ajuste de pontos experimentais
author: Wescley
"""

import matplotlib.pyplot as plt
import numpy as np
#primeiro abrimos o arquivo para podermos ler as informaçoes
f = open('millikan.txt','r')

data = f.readlines()
newdata = []
for n in data:
    newdata.extend(n.split())

#apos lidos os valores e atribuidos na variável newdata, agora separaremos as colunas 
#x e y em duas outras listas, xval e yval    
xval = []
yval = []
    
for n in range(newdata.__len__()):
    if ((n % 2) == 0):
        xval.append(float(newdata[n]))
    else:
        yval.append(float(newdata[n]))

#agora podemos fazer as operaçoes necessárias com os pontos
#quantidades deinidas no exercicios
ex = 0.0
ey = 0.0
exx = 0.0
exy = 0.0



#valor de Ex, Ey, Exx, Exy
for n in range(xval.__len__()):
    ex = ex + xval[n]
    ey = ey + yval[n]
    exx = exx + xval[n]**2
    exy = exy + xval[n]*yval[n]
ex = ex / xval.__len__()
ey = ey / yval.__len__()
exx = exx / xval.__len__()
exy = exy / xval.__len__()

#calculando os valores do coeficiente angular da reta(m) e o valor da constante(c)

m = (exy - ex*ey)/(exx - ex**2)
c = (exx*ey - ex*exy)/(exx - ex**2)

#gerando a funçao de ajuste 
x = np.linspace(0,max(xval)+0.1,150)
y = m * x + c

#adicionando os dados necessario ao grafico
#pontos experimentais
plt.scatter(xval,yval)
#funçao de ajuste
plt.plot(x,y)

plt.xlabel("v(hertz)")
plt.ylabel("V(volts)")

plt.show()

#como o problema do livro fornece a equaçao V = hv/e - phi, portanto a constante de planck (h)
#deve ser igual ao valor de m*e (onde e = carga do eletron)

planck = m *  1.602e-19

#portanto, o valor da constante de planck deve ser
print("Valor aceito da constante de planck: 6.62607004e-34")
print("Valor calculado da constante de planck: ",planck)



    

f.close()