import sys

T = int(sys.stdin.readline())


temp  = []
for tc in range(T):
    age, name = sys.stdin.readline().split()
    temp.append((int(age),tc, name))


temp.sort()
for i in temp:
    print(f'{i[0]} {i[2]}')







