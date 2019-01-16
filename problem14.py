def gradingStudents(grades):
    output=[]
    for x in grades:
        if x > 100 or x <0:
            output.append(-1)
            continue
        if x < 38:
            output.append(x)
        else:
            temp=round(x/5)*5
            if temp > x:
                output.append(temp)
            else:
                output.append(x)
    return output







n = int(input())

grades = []
for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)

result = gradingStudents(grades)
print(result)