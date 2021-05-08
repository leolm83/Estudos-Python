def is_prime(num):
    count=0
    for n in range(num+1):
        if n>0 and num%n==0:
            count+=1
    if count==2:
        return True
    else: 
        return False
