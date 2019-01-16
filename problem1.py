def digits(n):
    n=2**n
    count = 0
    temp = 10
    x=True
    while x:
        count = count+1
        if n<temp:
            x = False
        temp = temp * 10
    return count


tests = [
    (2, 1),
    (4, 2),
    (7, 3),
    (10, 4),
]

for test in tests:
    if digits(test[0])!=test[1]:
        print("Failed on value: "+str(test[0]))
        exit(1)