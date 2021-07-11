#Usos do Range em python
print("\t Dessa maneira exibe os numeros de 0 até fim-1")
# O argumento end="\t" no print define qual é o final do comando,
# normalmente após o print ele pula uma linha,
# mas com o/t ele dá apenas uma tabulacao e vai pra proxima instrucao
for num in range(10):
    print(num,end="\t")
print("\n \t Dessa forma ele exibe da posicao inicio até o fim-1")
#for num in range(incio,fim):
for num in range(1,11):
    print(num,end="\t")

print("\n É possivel alterar o incremento da funcao range tambem!")
numeros_pares=list(range(2,50,2))
print(f"\n \t\t\t{numeros_pares}")


print("\n \t É possivel criar listas tambem com a funcao range :")
lista=list(range(10))
print (f"\t\t{lista}")
