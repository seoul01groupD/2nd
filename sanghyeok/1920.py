import sys

T = int(sys.stdin.readline())
B = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

for i in C:
    if i in B:
        print(1)

    else:
        print(0)

