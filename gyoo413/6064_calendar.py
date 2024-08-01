T = int(input())
for tc in range(T):
    m, n, x, y = map(int, input().split())

    def gcd(a, b):
        x = min(a, b); y = max(a, b)
        while y % x != 0:
            temp = x
            x = y % x
            y = temp
        return x

    g = gcd(m, n)

    if g != 1 and (x % g == 0 or y % g == 0):
        print(-1)
    else:
        i = 1
        while True:
            if m == 1 and n == 1:
                print(1)
                break
            if i % m == x and i % n == y:
                print(i)
                break
            else:
                i += 1