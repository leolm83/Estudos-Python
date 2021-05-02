   def longest_consec(arr):
    theFirstBigger={"string":"","len":0,"index":""}
    for index,item in enumerate(arr):
        if(index+<len(arr)-1) and (len(arr[index]+arr[index+1])>theFirstBigger['len'])):
            theFirstBigger['len']=len(arr[index]+arr[index+1])
            theFirstBigger['string']=arr[index]+arr[index+1]
            theFirstBigger['index']=arr[index]
    return theFirstBigger['string']
