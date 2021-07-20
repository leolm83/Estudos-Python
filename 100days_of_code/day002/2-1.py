#somar todos os numeros em uma string
soma_caractere=0
string_numerica=input("Insira um numero com 2 digitos ou mais : ")
for caractere in string_numerica:
    if caractere in ["0","1","2","3","4","5","6","7","8","9"]:
        soma_caractere+=int(caractere)
print(f"A soma de todos os digitos em {string_numerica} é igual a {soma_caractere}")
