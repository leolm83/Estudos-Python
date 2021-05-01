###o programa recebe um numero e deve ordenar seus digitos em ordem decrescente ou seja :Input: 42145  resulta em Output: 54421
def descending_order(num):
    # Bust a move right here
    descOrder=[]
    stringDescOrder=""
    for n in str(num):
        descOrder.append(int(n))
    descOrder.sort(reverse=True)
    for item in descOrder:
        stringDescOrder+=str(item)
    return int(stringDescOrder)

/*outra forma de resolver o mesmo problema*/
def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num),reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')
