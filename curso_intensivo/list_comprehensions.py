print("Primeiros passos aos list comprehensions \n Da forma normal seria :")
squares=[]
for num in range(1,11):
    squares.append(num**2)
print(squares)
print("Em uma list comprehension isto seria :")
list_comprehension_squares=[numero**2 for numero in range(1,11)]
print(list_comprehension_squares)
