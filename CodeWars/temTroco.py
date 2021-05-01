/*The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line.
Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
 Exercicio sobre uma fila em que só é possivel vender se houver troco disponivel*/
def tickets(people):
    wallet={'25': 0,'50':0 ,'100':0}
    
    for payment in people:
        if payment==25:
            wallet['25']=wallet['25']+1
        if payment==50:
            if(wallet['25']>0):
                wallet['25']=wallet['25']-1
                wallet['50']=wallet['50']+1
            else:
                return "NO"
        if payment==100:
            if(wallet['25']>0 and wallet['50']>0 ):
                wallet['25']=wallet['25']-1
                wallet['50']=wallet['50']-1
                wallet['100']=wallet['100']+1
            elif(wallet['25']>2):
                wallet['25']=wallet['25']-3
                wallet['100']=wallet['100']+1
            else:
                return "NO"

    return "YES"
