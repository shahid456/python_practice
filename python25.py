def contacts(queries):
    string=[]
    count=[]
    for query in queries:
        if query[0] == 'add':
            string.append(query[1])
        elif query[0] == 'find':
            counter=0
            string = sorted(string)
            l=len(string)
            for z in range(l):
                if query[1][0] == string[z][0]:

                    while z<l and string[z][0:len(query[1])] != query[1] and query[1][0] == string[z][0]:
                        z=z+1
                    while(z<l and string[z][0:len(query[1])] == query[1] ):
                        counter+=1
                        z=z+1
                break

            count.append(counter)

    return count



queries_rows = int(input())

queries = []
string=input()
s=string.split('\n')
for query in s:
    queries.append(query.rstrip().split())
print(queries)
result = contacts(queries)
print(result)