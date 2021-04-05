###Diagonal topo direito p/ inferior esquerdo
tamanhoi=9
tamanhoj=9
for j in range(tamanhoj):
	print()
	for i in range(tamanhoi):
		if((j+i)==tamanhoi-1):
			print("MEIO", end =" ")	
		else:
			print(i, end =" ")
###Diagonal topo esquerdo p/ inferior direito
for j in range(tamanhoj):
	print()
	for i in range(tamanhoi):
		if(j==i):
			print("MEIO", end =" ")	
		else:
			print(i, end =" ")