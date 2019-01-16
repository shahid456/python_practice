def arrsum(arr,n):
    sum=0
    for x in range(n):
        sum=sum+arr[x]
    return sum


n=int(input('Enter num of elements in array'))
arr=[]
print('Enter the numbers\n')
for x in range(n):
    z=int(input())
    arr.append(z)
result=arrsum(arr,n)
print(result)