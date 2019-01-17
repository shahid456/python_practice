import numpy

def dynamicArray(n,queries):
    s=[]
    for i in range(n):
        s.append([])

    output=[]
    LA=0
    l=len(queries)
    for i in range(l):
        if queries[i][0] == 1:
            ind=(queries[i][1]^LA)%n
            s[ind].append(queries[i][2])
        elif queries[i][0] == 2:
            ind = (queries[i][1] ^ LA) % n
            z= queries[i][2]%(len(s[ind]))
            LA=s[ind][z]
            output.append(str(LA))
    return output







nq = input().rstrip().split()

n = int(nq[0])

q = int(nq[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

result = dynamicArray(n, queries)