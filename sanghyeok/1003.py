# def fibo(n):
#     if n < 2:
#         arr.append(n)
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)


def fibo2(n):
    f = [0] * (n+1)
    if n == 0:
        f[0] = 0
    elif n == 1:
        f[0] = 0
        f[1] = 1
    else:
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]

    return f

T = int(input())
for tc in range(T):
    N = int(input())
    count_0 = 0
    count_1 = 0
    print(fibo2(N))
    arr = fibo2(N)

    print(arr[-2], end= ' ')
    print(arr[-1])





