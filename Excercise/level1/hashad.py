def Hashad(n):
    hn = 0
    n = str(n)
    for i in range(len(str)):
        hn += n[i]
    return True if int(n) % hn == 0 else False


'''
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

//sum 을 생각 못했다!!
'''