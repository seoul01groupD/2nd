import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocketmon_dict = {}
pocketmon_list = []
for i in range(n):
    pocketmon = input().rstrip()
    pocketmon_dict.update({pocketmon: (i + 1)})
    pocketmon_list.append(pocketmon)

question = []
for j in range(m):
    question.append(input().rstrip())

for q in question:
    if q.isdigit():
        print(pocketmon_list[int(q) - 1])
    else:
        print(pocketmon_dict[q])

