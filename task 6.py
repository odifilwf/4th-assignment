def isPrime(n):
    s = 0
    for i in range(2,n):
        if n % i == 0:
            s+=1
            break
    if s == 0:
        return True
    else:
        return False
def isPrimeHelper(a,b):
    c = 0
    for i in range(a,b+1):
        if isPrime(i):
            c += 1
    print(c,end=" ")
isPrimeHelper(10,30)
