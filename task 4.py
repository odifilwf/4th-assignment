def printMatrix(n,m):
    j = 1
    for i in range(1,n*m+1):
        print(i,end=" ")
        if j % m == 0:
            print()
        j+=1
printMatrix(7,8)