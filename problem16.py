def camelcase(s):
    counter=1
    for x in s:
        temp=ord(x)
        if temp > 64 and temp < 91:
            counter+=1
    return counter



s = input()

result = camelcase(s)
print(result)