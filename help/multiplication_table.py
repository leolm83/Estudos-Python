def multiplication_table(number):
    multiplier=1
    while multiplier<=5:
        result=number*multiplier
        if result>25:
            #print(f"O resultado de {number} X {multiplier} é {result} e portanto é maior que 25 \n Fim da Execucao")
            break
        print(f"{number} X {multiplier} = {result}",end="\t")
        multiplier+=1
    print("")
multiplication_table(3)
multiplication_table(5)
multiplication_table(8)
