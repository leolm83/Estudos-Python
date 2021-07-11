#DEFINICAO DE COMPOSTO:
#UM NÚMERO NATURAL É COMPOSTO QUANDO TEM MAIS DE DOIS DIVISORES NATURAIS DISTINTOS
#DEFINICAO DE NUMERO PRIMO: 
#   UM NUMERO NATURAL PRIMO É AQUELE QUE POSSUI SOMENTE DOIS DIVISORES NATURAIS DISTINTOS:
#   O NUMERO 1 E ELE MESMO
# PS: O UNICO NUMERO PRIMO QUE É PAR É O NUMERO 2
# E OS NUMEROS 0 E 1 NAO SE ENCAIXAM NA DEFINICAO DE PRIMOS
# POIS NO CASO DO 1 O DIVISOR PRECISA SER DISTINTO (1/1==1/1)
# E NO CASO DO 0 É IMPOSSIVEL DIVIDIR POR 0 
primos=[2]
compostos=[]
for num in range(3,100,2):
    divisivel=0
    for div in range(1,num+1):
        #print(f"\n {num}/{div}=={num%div}")
        if(num%div==0):
            divisivel+=1
    #print(f"O numero :{num} foi divisivel {divisivel} vezes")
    if(divisivel==2):
        #print("Portanto ele é primo")
        primos.append(num)
    else:
        #print("Portanto ele é composto")
        compostos.append(num)
print(primos)
print(compostos)
