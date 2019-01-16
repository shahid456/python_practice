def twostring(string=""):
    x=string.split('\n')
    num=int(x[0])
    output=[]
    count=0
    check=-1
    for z in range(1,num+1):
        s1=x[z+count]
        count=count+1
        s2=x[z+count]
        for i in s1:
           check=s2.find(i)
           if check is not -1:
               output.append("YES")
               break

        if check is -1:
            output.append("NO")
        check=-1

    return output

out=twostring("3\nHello\nWorld\nbe\ncool\nYES\nNO")
print(out)