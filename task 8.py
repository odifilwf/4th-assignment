def decimalToBinary(n):
    if n == 0:
        print("0")
    b = ""
    while n > 0:
        r = n % 2
        b += str(r)
        n //= 2
    print(b)
decimalToBinary(13)