def isPalindrome(n):
    o_n = n
    r = 0
    while n > 0:
        d = n % 10
        r = r * 10 + d
        n = n // 10
    if r == o_n:
        print("Palindrome")
    else:
        print("Not Palindrome")

isPalindrome(11)