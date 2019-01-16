def angryProfessor(k,a):
    count=0
    for x in a:
        if x <= 0:
            count+=1
    if count >= k:
        return "NO"
    return "YES"



t = int(input())

for t_itr in range(t):
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)
