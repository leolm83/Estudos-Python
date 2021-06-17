tentativas=3
numeroSecreto=90
while(tentativas>0):
    numeroDigitado=int(input("Digite sua Tentativa \n"))
    if numeroSecreto==numeroDigitado:
        tentativas-=1
        print(f"Parabéns você acertou!!! o numero secreto é {numeroSecreto} e ainda lhe restaram {tentativas} tentativas")
        break
    elif numeroSecreto>numeroDigitado:
        print("O numero digitado é menor que o numero secreto")
        tentativas-=1    
    else:
        print("O numero digitado é maior que o numero secreto")
        tentativas-=1
print("Fim da execucao")
