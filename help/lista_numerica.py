numero=0
lista_numeros=[]
while numero>-1:
    numero=int(input("Adicione o número : "))
    if(numero>-1):
        lista_numeros.append(numero)
procura=int(input("Qual número você deseja procurar? "))
quantidade=0
for item in lista_numeros:
    if item==procura:
        quantidade+=1
print("o número "+str(procura)+" apareceu "+str(quantidade)+" vezes")
# vou procurar a fórmula da porcentagem
# em relação ao total e já volto
total_elementos=len(lista_numeros)
porcentagem=(quantidade/total_elementos)*100
print(" O valor "+str(procura)+" apareceu "+str(quantidade)+" de um total de "+str(total_elementos)+" elementos, o que corresponde a "+"{:.2f}".format(porcentagem)+"%")
