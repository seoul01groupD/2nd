# 2491
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

# 증가하는 수열을 나타내는 함수
def increase(arr,N):
    count = []
    c = 1
    for i in range(N):
        if arr[i] >= arr[i-1]:
            c += 1
            count.append(c)
        else:
            c = 1
    count.append(c)
    return max(count)

# 감소하는 수열을 나타내는 함수
def decrease(arr,N):
    count = []
    c = 1
    for i in range(N):
        if arr[i] <= arr[i-1]:
            c += 1
            count.append(c)
        else:
            c = 1
    count.append(c)
    return max(count)

# 증가/감소하는 값 중 최댓값 출력
max_count = max(increase(arr,N),decrease(arr,N))

if max_count > N:
    max_count -= 1
print(max_count)