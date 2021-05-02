def longest_consec(arr, k):
    theFirstBigger=""
    minorIndex=len(arr)-1
    for index,item in enumerate(arr):
        if(index+k-1<len(arr)):
            aux=""
            for j in range(k):
                aux+=arr[index+j]
            if(len(aux)>len(theFirstBigger)):
                theFirstBigger=aux
    return theFirstBigger
##https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

###outra solucao
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result
