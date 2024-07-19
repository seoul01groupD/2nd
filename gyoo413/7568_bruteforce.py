import sys

n = int(sys.stdin.readline())
people = []
for i in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))


for i in range(n):
    cnt = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    print(cnt, end = ' ')