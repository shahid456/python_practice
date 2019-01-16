def digits(n):
    count = 0
    temp = 10
    x=True
    while x:
        count = count+1
        if n<temp:
            x = False
        temp = temp * 10
    return count

def findDigits(num):
    out=[]
    for x in num:
        d=digits(x)
        temp=x
        counter=0
        for z in range(d,0,-1):
            div=pow(10,z-1)
            d=temp//div
            if d is not 0:
                k=x%d
                if k is 0:
                    counter=counter+1
            temp=temp-d*div
        out.append(counter)
    return out

t = int(input())
n=[]
for t_itr in range(t):
    n.append(int(input()))
print(n)
result = findDigits(n)
print(result)