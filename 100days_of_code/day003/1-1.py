#ANO BISSEXTO
# um ano é bissexto se for divisivel por 4 e nao ser divisivel por 100 ou ser divisivel 4 por 100 e tambem por 400
ano=int(input("Digite um ano para saber se ele é bissexto : "))
if(ano%4)==0:
    if(ano%100==0):
        if(ano%400==0):
            print(f"O ano {ano} é bissexto !")
        else:
            print(f"O ano {ano} não é bissexto")
    else:
        print(f"O ano {ano} é bissexto !")
else:
    print(f"O ano {ano} não é bissexto")
