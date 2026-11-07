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
n = int(input("Enter a number: "))
if isPrime(n) is True:
    print("Prime")
elif isPrime(n) is False or n == 1:
    print("Not prime")
