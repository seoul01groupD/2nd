import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst = sorted(lst, key=lambda lst: (lst[0], lst[1]))

meeting = []
small = lst[0][1]
duration = lst[0][1] - lst[0][0]
select = lst[0]

for idx in range(1, len(lst)):

    if (lst[idx][0] < small) and (lst[idx][1] - lst[idx][0] < duration):
        select = lst[idx]
        duration = lst[idx][1] - lst[idx][0]
        small = lst[idx][1]

    elif lst[idx][0] >= small:
        meeting.append(select)
        select = lst[idx]
        duration = select[1] -select[0]
        small = select[1]

    if idx == len(lst) - 1:
        meeting.append(select)
    print(select)
print(meeting)


print(len(meeting))

