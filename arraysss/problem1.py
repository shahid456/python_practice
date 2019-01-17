def hourglass(a):
    sum=[]
    for i in range(4):
        for j in range(4):
            temp=a[i][j]+a[i][j+1]+a[i][j+2]+a[1+i][1+j]+a[2+i][j]+a[2+i][1+j]+a[2+i][2+j]
            sum.append(temp)

    sum.sort(reverse=True)
    x=sum[0]
    return x
arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
a=hourglass(arr)
print(a)