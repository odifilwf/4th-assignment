def gcd (a,b):
    c = 0
    if a > b:
        for i in range(1,b+1):
            if a % i == 0 and b % i == 0:
                c = i
    if b > a:
        for i in range(1,a+1):
            if b % i == 0 and a % i == 0:
                c = i
    print(f"GCD = {c}")
gcd(24,36)