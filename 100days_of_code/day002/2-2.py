#EXERCISE 2.2
#CALCULADORA DE IMC
peso=float(input("Insira o seu peso em Kg : "))
altura=float(input("Insira sua altura em Metros : "))
imc=peso/altura**2
print(f"Seu imc é igual a :{imc:.2f}")
if(imc<18.5):
    print("E você está no indice de Abaixo do peso")
elif(imc<25):
    print("E você está no indice de peso normal")
elif(imc<30):
    print("E você está no indice acima do peso")
else:
    print("E você está no indice Obeso")
