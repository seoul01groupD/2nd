
def char(arr):
    stack = []
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')' or i == ']':
            if stack == []:
                return False

            else:
                if (i == ')' and stack[-1] != '(') or (i == ']' and stack[-1] != '['):
                    return False
                stack.pop()
    return not stack



while True:
    arr = input()
    if arr == ".":
        break
    if char(arr):
        print("yes")
    else:
        print("no")





