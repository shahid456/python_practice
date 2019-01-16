def chocolateFeast(n, c, m):
    output=[]
    w=n//c
    output.append(w)
    while w>=m:
        w_c=w//m
        output.append(w_c)
        w=w_c + w - w_c*m
    return sum(output)

t = int(input())

for t_itr in range(t):
    ncm = input().split()

    n = int(ncm[0])

    c = int(ncm[1])

    m = int(ncm[2])

    result = chocolateFeast(n, c, m)
    print(result)