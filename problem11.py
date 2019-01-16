def reverseArray(a):
    l=len(a)
    l=l-1
    temp=[]
    for i in range(l+1):
        temp.append(a[l-i])
    return temp


arr_count = int(input('Enter the number of Elements of Array'))
print("Enter Array's Element")
arr=[]
for i in range(arr_count):
    arr.append(int(input()))
print('Original Array:', arr)
res = reverseArray(arr)
print('Reversed Array:',res)