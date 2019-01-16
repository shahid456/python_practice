n=int(input("Enter the value of 'n'"))
x=int(input("Enter the value of 'x'"))

sum=n
p=0
k=pow(x,p)
powers=[]
temp=0
while k<=sum:
   for z in powers:
       temp=temp+pow(x,int(z))
   if temp is n:
       break
   elif k<sum:
       p+=1
       k=pow(x,p)
   if k>=sum:
        if k is sum:
            powers.append(str(p))
            k=pow(x,p)
        else:
            p=p-1
            powers.append(str(p))
            k=pow(x,p)
        p=0
        temp=temp+k
        sum=n-temp
        temp=0
        k=pow(x,p)


print(powers)