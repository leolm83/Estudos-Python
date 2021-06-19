def ContabilizaHoras(totalHoras):
    if(totalHoras>=5):
        valorFinal=4.80
        totalHoras-=4
        valorFinal+=2.0*totalHoras
        return valorFinal
    elif(totalHoras<5):
        valorFinal=0.0
        while(totalHoras>0):
            if(totalHoras>2):
                valorFinal+=1.40
                totalHoras-=1
            else:
                valorFinal+=1.0
                totalHoras-=1
        return valorFinal
        
horaEntrada= int(input("Hora entrada : "))
minutoEntrada=int(input("Minuto entrada : "))
horaSaida= int(input("Hora Saida : "))
minutoSaida= int(input("Minuto Saida: "))
if(horaEntrada>horaSaida):
    horasAPagar=(horaSaida+24)-horaEntrada
elif(horaEntrada<horaSaida):
    horasAPagar=horaSaida-horaEntrada
else:
    horasAPagar=0
minutosAPagar=minutoSaida-minutoEntrada
if(minutosAPagar>0):
    horasAPagar+=1
print("Minutos a Pagar : "+str(minutosAPagar))
print("Horas a pagar : "+str(horasAPagar))
print("Valor Final : " +str(ContabilizaHoras(horasAPagar)))
