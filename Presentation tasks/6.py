def isPrime(a,b):
    c = 0
    for i in range(a,b+1):
        flag = 0
        if i == 1:
            continue
        for j in range(2,i):
            if i % j == 0:
                flag = 1
        if flag == 0:
            c+=1
            print(i,end=" ")
    print("")
    print(c)
isPrime(1,100)