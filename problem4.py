def powerfun(n,d):
    p=0
    temp=pow(d,p)
    while(temp<=n):
        if temp is n:
            return 1
        p=p+1
        temp=pow(d,p)
    return 0

tests = [
    (64, 8, 1),
    (8, 2, 1),
    (16, 4, 1),
    (124, 8, 0),

]

for test in tests:
    if powerfun(test[0],test[1])!=test[2]:
        print("Failed on value: "+str(test[0])+' '+str(test[1]))
        exit(1)


