txt = "Hello, welcome to my world."

myChar="o"
count=0
indexes=[]
for index,value in enumerate(txt):
	if value==myChar:
		indexes.append(index)
		count+=1
print("O valor aparece "+str(count)+" vezes, nas posicoes :")
print(indexes)

