# Enter your code here. Read input from STDIN. Print output to STDOUT
def cap_room(Rooms):

    r=set(Rooms)
    for x in r:
        count=0
        z=0
        while z<len(Rooms):
            if x==Rooms[z]:
                count+=1
            if count>1:
                break
            z=z+1
        if count==1:
            return x

K=int(input())
Rooms=list(map(int,input().rsplit()))

r=set(Rooms)
print(cap_room(Rooms))

