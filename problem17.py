def extraLongFactorials(n):
    temp=n
    for x in range(n-1,0,-1):
        temp*=x
    return temp



n = int(input())
print(extraLongFactorials(n))