
/*Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']*/


def solution(s):
    lista=[]
    for index in range(0,len(s),2):
        if index+1<len(s):
         lista.append(s[index]+s[index+1])
        else:
            if len(s[index])==1:
                lista.append(s[index]+"_")
    return lista
