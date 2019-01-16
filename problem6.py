def mod(x,y):

    temp=pow(2,x)
    out=y%temp
    return out


tests = [
    (3, 14, 6),
    (4, 14, 14),
    (2, 8, 0),
]

for test in tests:
    if mod(test[0],test[1])!=test[2]:
        print("Failed on value: "+str(test[0])+' '+str(test[1]))
        exit(1)


