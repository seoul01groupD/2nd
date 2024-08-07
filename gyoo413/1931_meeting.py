import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst = sorted(lst, key=lambda lst: (lst[0], lst[1]))

meeting = []
start = lst[0][0]
end = lst[0][1]
select = lst[0]

for idx in range(1, len(lst)):

    if lst[idx][1] < end:
        select = lst[idx]
        start = lst[idx][0]
        end = lst[idx][1]

    elif lst[idx][0] >= end and lst[0] != start:
        meeting.append(select)
        select = lst[idx]
        end = select[1]

    if idx == len(lst) - 1:
        meeting.append(select)
   
print(len(meeting))

