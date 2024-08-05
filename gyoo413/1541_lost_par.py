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

next_lst = []
temp = lst[0]
for i in range(len(lst)):
    
    if lst[i] == '+':
        temp += lst[i + 1]
    elif lst[i] == '-':
        next_lst.append(temp)
        temp = lst[i + 1]
    if i == len(lst) - 1:
        next_lst.append(temp)

ans = next_lst[0]
for i in range(1, len(next_lst)):
    ans -= next_lst[i]

print(ans)
