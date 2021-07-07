com_espacos="  **COM ESPACOS**  "
print(com_espacos)
print(com_espacos.rstrip()+"#SEM A DIREITA#")
print(com_espacos.lstrip()+"#SEM A ESQUERDA#")
print(com_espacos.strip()+"#SEM ANTES E APOS#")
print(com_espacos+"ESTES METODOS NAO MODIFICAM A STRING ORIGINAL")

frase_espacada="A E B C Q"
nova_frase=""
print("Frase sem remocao de espacos: \n \t"+frase_espacada)
###DESSA FORMA REMOVE TODOS OS ESPACOS :
for letra in frase_espacada:
    
    if letra !=" ":
        nova_frase+=letra
print("Frase com remocao de espacos: \n \t"+nova_frase)
