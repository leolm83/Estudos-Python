import re

def to_camel_case(text):
    #your code here
    camelCase=""
    text=text.strip()
    texts=re.split(' |_|-|!|\+|\*|\"',text)
    for index,txt in enumerate(texts):
        if(index!=0): 
            camelCase+=txt.capitalize()
            
        else:
           camelCase+=txt.lower()
    return camelCase
