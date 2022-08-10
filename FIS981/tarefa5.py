# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:26:18 2017

@author: Wescley
"""

import matplotlib.pyplot as plt
import numpy as np

#Lendo do arquivo
data = np.loadtxt("sunspots.txt",float)

#filtrando o exercicio
op = input("Entre com a alternativa do exercicio (A, B ou C)")

#alternativa A
if (op.upper()=='A'):
    

    #alocando as variáveis
    x = data[:,0]
    y = data[:,1]

    #plotando o grafico
    plt.scatter(x,y,marker="+")

    #formatando o grafico
    plt.xlabel("Tempo(meses)")
    plt.ylabel("Sunspots")

    plt.show()
    
#alternativa B    
elif (op.upper()=='B'):


    #alocando as variáveis
    x = data[:1000,0]
    y = data[:1000,1]

    #plotando o grafico
    plt.scatter(x,y, marker="+")

    #formatando o grafico
    plt.xlabel("Tempo(meses)")
    plt.ylabel("Sunspots")

    plt.show()


    
#alternativa C    
elif (op.upper()=='C'):
    #alocando as variáveis
    x = data[:1000,0]
    y = data[:1000,1]
    #criando o vetor de running average    
    y1 = np.zeros(1000,float)
    
    #calculando o vetor running average para os valores válidos
    for i in range (4,x.size-4):
        y1[i] = (y[i-4] + y[i-3] + y[i-2] + y[i-1] + y[i] + y[i+1] + y[i+1] + y[i+2] + y[i+3] + y[i+4])/10
    #diferenciando os dois vetores 
    plt.plot(x,y,"b+")
    plt.plot(x,y1,"r")
    plt.show()
    
    
    
#alternativa INVALIDA
else:
    print("Opção não é válida")