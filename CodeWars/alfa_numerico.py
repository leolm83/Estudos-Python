import re
def alphanumeric(password):
    #pattern=r"([a-z]|[0-9]|[A-Z])"
    print(password)
    if len(password)!=0:
        for char in password:
            x=re.findall(r"([a-z]|[0-9]|[A-Z])",char)
            print(x)
            if len(x)==0:
                return False
        return True
    else: 
        return False
      
      #######################
      #METODO MELHOR E MAIS CURTO :
      #
      def alphanumeric(string):
    return string.isalnum()
