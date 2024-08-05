n = int(input())

tile = [1, 3]
for i in range(2, n):
    tile.append((2 * tile[i - 2] + tile[i - 1]) % 10007)

print(tile[n - 1])