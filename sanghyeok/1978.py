T = int(input())
arr = list(map(int, input().split()))
result = 0

for i in arr:
    if i == 1 or i == 0:
        result +=1
        continue
    for i2 in range(2,i):
        if i%i2 == 0:
            result+=1
            break
        else:
            continue






print(T-result)