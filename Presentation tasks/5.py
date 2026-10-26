def isPrime(n):
    flag = 0
    for i in range(2,n):
        if n % i == 0:
            flag = 1
    if flag == 0:
        return True
    else:
        return False
print(isPrime(11))
print(isPrime(12))