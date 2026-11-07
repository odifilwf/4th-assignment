def isArmstrong(n):
    num = n
    c = 0
    s = 0
    while num !=0:
        num //= 10
        c += 1
    num = n
    while num != 0:
        a = num % 10
        s += a ** c
        num //= 10
    if s == n:
        return True
    else:
        return False
for i in range(100,1000):
    if isArmstrong(i):
        print(i, end=" ")

