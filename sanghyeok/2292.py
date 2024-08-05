N = int(input())

result = 1
result2 = 0
for i in range(N):
    if N > result:
        result += 6*i
        result2 += 1
    elif N==1:
        result2 = 1
    else:
        result2 = i
        break
print(result2)