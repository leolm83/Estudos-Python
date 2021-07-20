#PROJECT DAY 2
#calculadora de gorjetas
print("Boas vindas à calculadora de gorjetas")
total_gastos=float(input("Qual é o valor total da conta ? "))
porcentagem_gorgeta=float(input("Qual a porcentagem de gojeta que voce deseja doar ? "))/100
#porcentagem_gorgeta=porcentagem_gorgeta/100
pessoas=int(input("Quantas pessoas irao dividir a conta ? "))
print(f" Cada pessoa deve pagar R${(total_gastos+total_gastos*porcentagem_gorgeta)/pessoas:.2f}")
