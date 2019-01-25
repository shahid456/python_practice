size=list(map(int,input().rsplit()))
n=size[0]
m=size[1]
Array=list(map(int,input().rsplit()))
A=set(list(map(int,input().rsplit())))
B=set(list(map(int,input().rsplit())))
happ=0
for x in Array:
    if x in A:
        happ+=1
    if x in B:
        happ-=1
print(happ)