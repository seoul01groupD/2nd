# 2108 ---> 시간초과

# 선택정렬
def Selection_Sort(arr,N):
    for i in range(N-1):
        min_idx = i   # 임의의 최솟값 인덱스 지정
        for j in range(i+1,N):   # 임의 최솟값을 제외한 나머지 범위
            if arr[min_idx] > arr[j]:   # 나머지 범위에서 최솟값을 찾으면
                min_idx = j   # i랑 위치 교환
        arr[i],arr[min_idx] = arr[min_idx],arr[i]   # 최솟값 업데이트
    return arr

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))
arr = Selection_Sort(arr,N)

n_sum = 0
for x in arr:
    n_sum += x

count = {}
for x in arr:
    count[x] = 0
for x in arr:
    count[x] += 1

a = 0
max_lst = []
for x in arr:
    if a <= count[x]:
        a = count[x]
        count_key = x
        max_lst.append(x)

if len(max_lst) > 1:
    mode = max_lst[1]
else:
    mode = max_lst[0]

# 산술평균
mean = int(round(n_sum/N,0))
# 중앙값
median = arr[N//2]
# 최빈값
if len(max_lst) > 1:
    mode = max_lst[1]
else:
    mode = max_lst[0]
# 범위
num_range = arr[-1] - arr[0]
print(mean, median, mode, num_range, sep='\n')