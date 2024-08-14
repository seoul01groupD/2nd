# 2116

# index 함수
def find_idx(arr,value):
    n = 0
    for x in arr:
        if x == value:
            return n
        else:
            n += 1
import copy
N = 5
dice = [[2,3,1,6,5,4],[3,1,2,4,6,5],[5,6,4,1,3,2],[1,3,6,2,4,5],[4,1,6,5,2,3]]
#  [list(map(int,input().split())) for _ in range(N)]

lst = copy.deepcopy(dice)
# lst_all =
sum_dice = 0

for i in range(5):
    sum_row = []
    for j in range(6):
        if i == 0:
            if j == 0:
                a,b = lst[i][0],lst[i][5]
            elif j == 1 or j == 2:
                a,b = lst[i][j],lst[i][j+2]
            elif j == 3 or j == 4:
                a, b = lst[i][j], lst[i][j - 2]
            else:
                a, b = lst[i][5], lst[i][0]
            dice[i].remove(a)
            dice[i].remove(b)
            sum_row.append(dice[i])
            break

        else:
            idx = find_idx(lst[i],b)
            if idx == 0:
                a,b = lst[i][0],lst[i][5]
            elif idx == 1 or idx == 2:
                a,b = lst[i][idx],lst[i][idx+2]
            elif idx == 3 or idx == 4:
                a, b = lst[i][idx], lst[i][idx - 2]
            else:
                a, b = lst[i][5], lst[i][0]
            dice[i].remove(a)
            dice[i].remove(b)
            sum_row.append(dice[i])
            break

    print(sum_row)
