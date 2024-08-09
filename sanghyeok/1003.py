def fibo(n):
    count_0[0] = 1
    count_1[0] = 0

    if n>0:
        count_0[1] = 0
        count_1[1] = 1

    for i in range(2, n+1):
        count_0[i] = count_0[i-1] + count_0[i-2]
        count_1[i] = count_1[i-1] + count_1[i-2]

    return count_0[n], count_1[n]





T = int(input())
for tc in range(T):
    N = int(input())
    count_0 = [0] * (N + 1)
    count_1 = [0] * (N + 1)
    result_0, result_1 = fibo(N)
    print(result_0, result_1)











