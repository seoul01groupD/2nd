n = int(input())

M = n // 5
m = 0

for i in range(M, -1, -1):
    if (n - 5 * i) % 3 == 0:
        m = (n - 5 * i) // 3
        print(i + m)
        break
else:
    print(-1)

