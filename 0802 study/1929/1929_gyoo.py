m, n = map(int, input().split())

prime_list = [True for x in range(n + 1)]

prime_list[0] = prime_list[1] = False

for i in range(2, int(n ** (1/2)) + 1):

    if prime_list[i] == True:
        j = 2
        while i * j <= n:
            prime_list[i * j] = False
            j += 1

for i in range(m, n + 1):
    if prime_list[i]:
        print(i)