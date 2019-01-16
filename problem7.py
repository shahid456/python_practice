def separate_number(q,string):
	output=[]
	for j in range(q):
		inp = string[j]
		if inp[0] == '0':
			print("NO")
			continue
		result = False
		for i in range(1,len(inp)//2+1):
			t = ""
			cur = int(inp[:i])
			check = 0
			while len(t) < len(inp):
				t =t+str(cur)
				cur =cur+ 1
				check =check+1
			if check > 1 and t == inp:
				output.append("YES")
				output.append(inp[:i])
				result = True
				continue
		if not result:
			output.append("NO")
	return output


q=int(input('Enter the number of queries'))
s=[]
for x in range(q):
	print('Enter string', x + 1, ' ')
	temp=input()
	s.append(temp)
res=separate_number(q,s)

print(res)