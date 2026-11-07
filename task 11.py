def lcm(a, b):
    def gcd(c, d):
        n = 0
        if c > d:
            for i in range(1, d + 1):
                if c % i == 0 and d % i == 0:
                    n = i
        if d > c:
            for i in range(1, c + 1):
                if c % i == 0 and d % i == 0:
                    n = i
        return n
    return abs(a * b) // gcd(a,b)

print(f"LCM = {lcm(6, 8)}")