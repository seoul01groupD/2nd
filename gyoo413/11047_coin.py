n, k = map(int, input().split())
coin =[]
for i in range(n):
    coin.append(int(input()))

cnt = 0

for i in range(len(coin) - 1, -1, -1):
    if coin[i] <= k:
        cnt += k // coin[i]
        k %= coin[i]

    if k == 0:
        break

print(cnt)