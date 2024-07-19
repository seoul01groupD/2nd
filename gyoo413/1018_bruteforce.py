import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

def black_or_white(color, x):
    if x % 2 == 0:
        return color[0]
    else:
        return color[1]

mini = m * n
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0 
        cnt2 = 0
        for a in range(8):
            for b in range(8):
                if board[i + a][j + b] != black_or_white(['W', 'B'], a + b):
                    cnt1 += 1
                if board[i + a][j + b] != black_or_white(['B', 'W'], a + b):
                    cnt2 += 1
        small = 0
        if cnt1 < cnt2:
            small = cnt1
        else:
            small = cnt2
        if small < mini:
            mini = small

print(mini)

