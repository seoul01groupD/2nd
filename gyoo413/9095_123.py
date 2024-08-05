T = int(input())
for tc in range(1, T + 1):
    lst = [1, 2, 4]
    for i in range(3, 12):
        lst.append(lst[i - 3] + lst[i - 2] + lst[i - 1])
    
    x = int(input())
    print(lst[x - 1])