n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst = sorted(lst, key=lambda lst: (lst[0], lst[1]))
print(lst)