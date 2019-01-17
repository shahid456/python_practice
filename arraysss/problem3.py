def matchingStrings(strings, queries):
    counter=0
    count=[]

    lq=len(queries)
    ls=len(strings)
    for x in queries:
        counter=0
        for j in range(ls):
            if x == strings[j]:
                counter+=1
        count.append(str(counter))
    return count







strings_count = int(input())

strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

res = matchingStrings(strings, queries)
for x in res:
    print(x)