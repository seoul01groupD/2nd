T = int(input())
arr = [[0] * 6 for _ in range(T)]
for tc in range(T):
    arr[tc] = list(map(int, input().split()))

temp = [[]*5 for _ in range(5)]
for i in range(5):
    A,F = arr[i][0], arr[i][5]
    B,D = arr[i][1], arr[i][3]
    C,E = arr[i][2], arr[i][4]
    temp[i].append([A,F])
    temp[i].append([B,D])
    temp[i].append([C,E])

print(temp)




