def saveThePrisoner(p, c, s):
    return (s-1+c-1)%p+1

t = int(input())

for t_itr in range(t):
    nms = input().split()

    n = int(nms[0])

    m = int(nms[1])

    s = int(nms[2])
print(saveThePrisoner(n,m,s))