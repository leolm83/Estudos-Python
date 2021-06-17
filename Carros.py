ModeloCarros=[]
Combustivel=[]
for x in range(4):
    ModeloCarros.append(input("Digite o Modelo do Carro : "))
    Combustivel.append(int(input("Digite quantos Km o carro faz com 1 litro : ")))
for index,item in enumerate(ModeloCarros):
    combustivelMilKm=1000/Combustivel[index]
    print(f" O modelo :{item} faz {Combustivel[index]} por litro,\n entao em para percorrer 1000 serao necessarios {combustivelMilKm:.2f} e serao gastos {combustivelMilKm*2.5:.2f}") 
