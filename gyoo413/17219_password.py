import sys
input = sys.stdin.readline

n, m = map(int, input().split())
password = {}
for i in range(n):
    k, v = input().split()
    k.strip(); v.strip()
    password.update({k: v})

finding = []
for i in range(m):
    finding.append(input().rstrip())

for find in finding:
    print(password[find])