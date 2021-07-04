""""Como usar replace em apenas um caractere?
Ex:
letra = 'a'
Palavra = "----"
Palavra = Palavra.replace(palavra[0], letra)
Ele acaba substituindo todos os caracteres 
Retornando:
>> aaaa
Usei a posição 0, mas pode ser qualquer outra"""

letra='a'
palavra='-----'
novaPalavra=""
for indice,item in enumerate(palavra):
	novaPalavra+=item
	if indice==0:
		novaPalavra+=item.replace('-',letra)
print(novaPalavra)
