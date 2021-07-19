#EXERCISE 1.4 Switch Values with Variables
#trocando valores de variaveis inteiras sem uma variavel auxiliar
a=int(input("Insira um numero:"))
b=int(input("Insira outro numero:"))

a+=b
b=a-b
a=a-b
print("A "+ str(a))
print("B "+ str(b))
