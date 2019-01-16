def palindrome(string):
    x=string.split('\n')
    size=int(x[0])
    output=[]
    for k in range(1,size+1):
        temp=x[k]
        i=0
        j=-1
        if temp[::-1]==temp:
            output.append(-1)
            continue
        if(len(temp)%2==0):
            length=len(temp)//2-1
        else:
            length=(len(temp)//2)
        while i<=length:
            if temp[i]==temp[j]:
               pass
            else:
                if  i is not length and temp[i]==temp[j-1]:
                    temp1=temp
                    temp=temp.replace(temp[j],'')
                    if temp[::-1]==temp:
                        output.append(len(temp)+j+1)

                    elif temp1[j]==temp1[i+1]:
                        temp1 = temp1.replace(temp[i], '')
                        if temp1[::-1] == temp1:
                            output.append(i)
                        else:
                            output.append(-1)
                    else:
                        output.append(-1)
                    break

                elif i is not length and temp[j]==temp[i+1]:
                    temp = temp.replace(temp[i], '')
                    if temp[::-1] == temp:
                        output.append(i)
                    else:
                        output.append(-1)
                    break
                elif i is length:
                    if temp[i]==temp[j]:
                        output.append(-1)
                    else:
                        output.append(i)
                    break
                else:
                    output.append(-1)
                    break

            i=i+1
            j=j-1

    return output




string="1\naaa"
out=palindrome(string)

print(out)