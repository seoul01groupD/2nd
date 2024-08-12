# 10989 -----> 메모리, 시간 초과 해결

# Counting Sort + sys 사용
import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(N):
    i = int(sys.stdin.readline())
    arr[i] += 1

for i in range(1,10000):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)