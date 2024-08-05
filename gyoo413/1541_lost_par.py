equation = list(input())

lst = []
temp = ''
for i in range(len(equation)):
    if equation[i].isdigit():
        temp = temp + equation[i]
    else:
        lst.append(int(temp))
        lst.append(equation[i])
        temp = ''
    if i == len(equation) - 1:
        lst.append(int(temp))
        temp = ''

print(lst)
