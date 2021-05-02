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
