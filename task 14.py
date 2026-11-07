def transformDigits(n):
    r = 0
    m = 1
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            d += 1
        else:
            d -= 1
        r = d * m + r
        m *= 10
        n //= 10
    return r
print(transformDigits(983210))