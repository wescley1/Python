# -*- coding: utf-8 -*-
"""

"""
import math as mt

def bin(N,K):
    if (K==0):
        return 1
    else:
        return mt.factorial(N)/(mt.factorial(K)*mt.factorial(N-K))
    

#controlador para selecionar a alternativa a ser executada
op = input("Entre com a alternativa do exercicio(A, B ou C)")

#alternativa A
if (op.upper()=='A'):
    #entrada de valores
    n = int(input("Entre com o valor de N(inteiro)"))
    k = int(input("Entre com o valor de K(inteiro)"))
    print("O coeficiente binomial de", n," e",k," é :", int(bin(n,k)))

#alternativa B
elif (op.upper()=='B'):
    print("Triangulo de pascal até a linha 20")
    #primeiro é definido uma string vazia
    linha = ''
    #utiliza-se dois loops de for para preenchimento do triangulo
    #obs.: as 20 primeiras linhas compreendem de 0 até 19
    for i in range(20):
        for j in range(i+1):
            #preenchimento de cada linha completa do triangulo concatenando os valores
            linha = linha + str(int(bin(i,j))) + ' '
        #printa a linha no final da execuçao do segundo for    
        print(linha)
        #reseta a linha para ser preenchida novamente
        linha = ''

#alternativa C        
elif (op.upper()=='C'):
    #calcula a probabilidade de acordo com a formula passada
    res = bin(100,60)/(2**100)
    print ("A probbilidade de serem exatamente 60 caras será %.2f" % res) 
    
    #calcula a probabilidade com o complementar de todos os valores de 0 até 59
    maior60 = 0
    for i in range(59):
        maior60 = maior60 + ((bin(100,i))/(2**100))
    print ("A probabilidade de serem 60 ou mais caras será %.2f" % (1 - maior60))

#caso de alternativa inválida
else:
    print("Alternativa nao é válida")






