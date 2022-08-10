def defineConst(massaAtom,numAtom):
    if ((numAtom%2 == 0) and ((massaAtom-numAtom)%2 == 0)):
        return int(12)
    elif ((numAtom%2 != 0) and ((massaAtom-numAtom)%2 != 0)):
        return int(-12)
    else:
        return int(0)


#definindo as constantes do problema
a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

op = str(input("Entre com a alternativa do exercicio(A, B ou C)"))

#alternativa A
if (op.upper() == 'A'):
    
    #entrada dos valores
    A = int(input("Entre com o valor da massa do átomo: "))
    Z = int(input("Entre com o número atomico do átomo: "))

    #atribui o valor da constante a5
    a5 = defineConst(A,Z)
                
    #calcula o valor da energia total de ligação
    B = a1*A - a2*(A**(2/3)) - a3*(Z**2)/(A**(1/3)) - a4*((A-2*Z)**2)/(A) + a5/(A**(1/2))
    #arredonda o valor para ficar mais apresentável
    B = round(B,2)
    print("A energia de ligação por núcleon será %.2f" % (B/A) ,"MeV")
    
#alternativa B
elif (op.upper() == 'B'):
    
    #entrada de dados
    Z = int(input("Entre com o número atomico do átomo: "))
    
    #variavel que receberá o maior valor de ligação por nucleons
    maior = -99999
    #variavel que receberá a massa do maior valor da ligação por nucleons
    massaMaior = 0
    #loop para percorrer todos os valores de massa entre z e 3z
    for i in range(Z,3*Z):
        #atribui valor da constante a5
        a5 = defineConst(i,Z)
        #calcula a energia total de ligação
        B = a1*i - a2*(i**(2/3)) - a3*(Z**2)/(i**(1/3)) - a4*((i-2*Z)**2)/(i) + a5/(i**(1/2))
        #compara o valor atual de ligação por nucleon com o maior salvo até o momento
        if ((B/i) > maior):
            maior = B/i
            massaMaior = i
    #arredonda para ficar mais apresentável
    maior = round(maior, 2)        
    print ("O maior valor de energia de ligação por nucleon será o núcleon de massa", massaMaior," com a energia de ", maior, "MeV")
    
#alternativa C
elif (op.upper() == 'C'):
    
    #variavel que receberá o maior valor de ligação por nucleons
    maior = -99999
    #variavel que receberá a massa do maior valor da ligação por nucleons
    massaMaior = 0
    #variável para armazenar o maior valor de ligação por nucleons entre todos os atomos avaliados
    maiorEnergiaLigacao = -99999
    #variavel para armazenar o numero atomico do maior valor de ligação por nucleons
    maiorEnergiaLigacaoAtom = 0
    
    #loop para percorrer todos os atomos de numero atomico entre 1 e 100
    for i in range (1,101):
        #loop para percorrer todos os valores de massa entre z e 3z
        for j in range(i,3*i):
            #define a constante a5
            a5 = defineConst(j,i)
            #calcula energia total de ligação
            B = a1*j - a2*(j**(2/3)) - a3*(i**2)/(j**(1/3)) - a4*((j-2*i)**2)/(j) + a5/(j**(1/2))
            #avalia o valor atual de energia de ligação por nucleons e compara com o maior armazenado
            if ((B/j) > maior):
                maior = B/i
                massaMaior = j
            #avalia o valor atual de ligação por nucleons com o maior entre todos os avaliados
            if ((B/j) > maiorEnergiaLigacao)    :
                maiorEnergiaLigacao = B/j
                maiorEnergiaLigacaoAtom = i
        #imprime os valores para cada numero atomico
        print("O valor mais estável de massa para o número atomico ", i, " é A =", massaMaior)            
        #reseta os valores para avaliar o proximo numero atomico
        maior = -99999
        massaMaior = 0;
    print("A energia máxima de ligação por nucleon ocorre no atomo de numero atomico", maiorEnergiaLigacaoAtom)        
