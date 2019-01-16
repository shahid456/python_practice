def fairRations(B):
    count=0
    for x in range(len(B)-1):
        if B[x]%2!=0:
            B[x]+=1
            B[x+1]+=1
            count+=2
    check=0
    for x in B:
        if x%2==0:
            check+=1
    if check==len(B):
        return count
    return "NO"





N = int(input())

B = list(map(int, input().rstrip().split()))

result = fairRations(B)
print(result)