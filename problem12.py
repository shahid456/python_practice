def left_rot(arr,d):
    l=len(arr)
    temp=arr[d:l]+arr[0:d]
    return temp

t=left_rot(list(map(int, input().rstrip().split())),7)
print(t)