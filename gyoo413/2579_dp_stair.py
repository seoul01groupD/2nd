n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
if n > 1:
    score_list = [[lst[0], 0], [lst[0] + lst[1], lst[1]]]

    for i in range(2, n):
        score_list.append([score_list[i - 1][1] + lst[i], max(score_list[i - 2][0], score_list[i - 2][1]) + lst[i]])

    maximum = max(score_list[n - 1][0], score_list[n - 1][1])
    print(maximum)

else:
    print(lst[0])