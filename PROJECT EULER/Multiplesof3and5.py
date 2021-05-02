#Exercise 1 : Multiples of 3 and 5
sum=0
for x in range(10):
	if(x%3==0 or x%5==0):
		sum+=x
print(sum)
