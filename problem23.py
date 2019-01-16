def workbook(n, k, arr):
    count=0
    pg=0
    for x in arr:
        prev_prob=1
        z=0
        temp=x
        while temp>0:
            if temp-k>=0:
                temp=temp-k
                z+=k
            else:
                z+=temp
                temp=-1
            pg=pg+1
            if prev_prob<=pg and pg<=z:
                count=count+1
            prev_prob=z+1
    return count








nk = input().split()

n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
result = workbook(n, k, arr)
print(result)