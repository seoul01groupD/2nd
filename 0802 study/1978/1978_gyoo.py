n = int(input())
num = list(map(int, input().split()))


def find_prime(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        prime = 1
        for i in range(2, n):
            if n % i == 0:
                prime = 0
                break
            else:
                continue
        return prime


cnt = 0
for p in num:
    cnt += find_prime(p)

print(cnt)