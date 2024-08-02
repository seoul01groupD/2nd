T = int(input())
for tc in range(T):
    m, n, x, y = map(int, input().split())
    if x == m:
        x = 0
    if y == n:
        y = 0

    def gcd(a, b):
        x = min(a, b); y = max(a, b)
        while y % x != 0:
            temp = x
            x = y % x
            y = temp
        return x

    g = gcd(m, n)

    if g != 1 and abs(x - y) % g != 0:
        print(-1)
    else:
        i = 0
        while True:
            if m == 1 and n == 1:
                print(1)
                break
            if (m * i + x) % n == y and (m * i + x) > 0:
                print(m * i + x)
                break
            else:
                i += 1