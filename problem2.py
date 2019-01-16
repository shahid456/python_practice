def powerfun(num):
    from math import sqrt
    if num==1:
        return True
    for x in range(2,int(sqrt(num))+1):


        y=1
        p=1
        while (p <= num):
            p=pow(x,y)
            y=y+1
            if (p == num):
                return True
    return False

tests = [
    (2, 0),
    (8, 1),
    (7, 0),
    (16, 1),
    (24, 0),
    (9, 1),
    (27, 1)
]

for test in tests:
    if powerfun(test[0])!=test[1]:
        print("Failed on value: "+str(test[0]))
        exit(1)



