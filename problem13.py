def min_max(arr):
    min=arr[0]
    max=arr[0]
    sum=0
    l=len(arr)
    for x in range(l):
        if min > arr[x]:
            min=arr[x]
        if max < arr[x]:
            max=arr[x]
        sum=sum+arr[x]
    temp=max
    max=sum-min
    min=sum-temp
    print(max,'  ',min)
min_max([1,2,3,4,5])