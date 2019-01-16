def howManyGames(p, d, m, s):
    count=0
    if s < p:
        return 0
    else:
        s=s-p
        temp=p
        count+=1
        while s-m >=0 :
            if (temp - d) > m:
                temp=temp-d
                s=s-temp
                if s>=0:
                    count+=1
            else:
                s=s-m
                if s>=0:
                    count+=1
    return count


pdms = input().split()

p = int(pdms[0])

d = int(pdms[1])

m = int(pdms[2])

s = int(pdms[3])

answer = howManyGames(p, d, m, s)
print(answer)