import sys
input = sys.stdin.readline

m, n = map(int, input().split())
lst = list(map(int, input().split()))
for idx in range(1, m):
    lst[idx] += lst[idx - 1]
lst.insert(0, 0)

for _ in range(n):
    x, y = map(int, input().split())
    print(lst[y] - lst[x - 1])
