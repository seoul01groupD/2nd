calculation = list(input())
stack = []
result = []
isp = 1
for char in calculation:
    if char == '*' or char == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result.append(stack.pop())
        stack.append(char)
        isp = 2
    elif char == '+' or char == '-':
        if isp == 1:
            while stack and (stack[-1] == '+' or stack[-1] == '-'):
                result.append(stack.pop())
            stack.append(char)
        elif isp == 2:
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(char)
            isp = 1
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    else:
        result.append(char)
while stack:
    result.append(stack.pop())

for char in result:
    print(char, end='')