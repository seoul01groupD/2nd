# 2108 ---> 시간초과
# 선택정렬을 사용하려 했으니 시간초과로 사용X

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

# 리스트 정렬
arr = sorted(arr)

# 최빈값
count = {}
for x in arr:
    count[x] = 0
for x in arr:
    count[x] += 1

mode_lst = []
for k, v in count.items():
    if v == max(count.values()):
        mode_lst.append(k)

# 산술평균
mean = int(round(sum(arr)/N,0))
# 중앙값
median = arr[N//2]
# 최빈값
if len(mode_lst) > 1:
    mode = mode_lst[1]
else:
    mode = mode_lst[0]
# 범위
num_range = arr[-1] - arr[0]

print(mean, median, mode, num_range, sep='\n')