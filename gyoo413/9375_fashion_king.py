import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    
    n = int(input())

    fashion = {}

    for i in range(n):
        v, k = input().split()
        v.strip(); k.strip()
        
        if not fashion.get(k):
            fashion.update({k: 1})
        else:
            fashion[k] += 1

    ans = 1
    for v in fashion.values():
        ans *= (v + 1)

    print(ans - 1)