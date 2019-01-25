n = int(input())
s = set(map(int, input().split()))
c=int(input())
for _ in range(c):
    command=input()
    if command[0]=='p':
        s.pop()
    elif command[0]=='r':
        val=int(command[7:len(command)])
        s.remove(val)
    else:
        val=int(command[7:len(command)])
        s.discard(val)
print(sum(s))

