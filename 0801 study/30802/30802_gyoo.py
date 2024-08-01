n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = 0
for i in range(len(size)):
    if size[i] % t == 0:
        cnt += (size[i] // t)
    else:
        cnt += ((size[i] // t) + 1)

print(cnt)
print(n // p, n % p)