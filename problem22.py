def serviceLane(width, cases):
    output=[]
    for case in cases:
        temp=width[case[0]:case[1]+1]
        output.append(min(temp))
    return output

nt = input().split()

n = int(nt[0])

t = int(nt[1])

width = list(map(int, input().rstrip().split()))

cases = []

for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))

result = serviceLane(width, cases)
print(result)