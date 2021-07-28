num=''
while (num==''):
    try:
        num =int(input("insira um numero : "))
    except ValueError :
        num=''
    else:
        print(num)
        #Esse bloco so será executado se o try passar e nao houver erro!!!
    