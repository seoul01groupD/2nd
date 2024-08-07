
T = int(input())
lst = []
for tc in range(T):
    N = int(input())
    lst.append(N)
stack = []
for i in lst:
    if stack ==[]:
        stack.append(i)
    elif i == 0:
        stack.pop()
    else:
        stack.append(i)

result = sum(stack)
print(result)
