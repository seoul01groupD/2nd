import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_set = set()
m_set = set()

for i in range(n):
    n_set.add(input().strip())

for j in range(m):
    m_set.add(input().strip())

name = sorted(list(n_set & m_set))
print(len(name))
print('\n'.join(name))