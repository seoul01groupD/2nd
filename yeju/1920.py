# 1920

# 선택정렬, 퀵정렬 구현 -> 런타임에러

# 이진검색
def binary_search(arr,start,end,t):
    middle = (start + end) // 2   # 중간을 기준으로
    if start <= end:   # start가 end 보다 작거나 같은 범위 내에서
        if arr[middle] < t:   # 타겟이 중간값보다 크면,
            return binary_search(arr,middle+1,end,t)   # start를 middle +1로
        elif arr[middle] > t:   # 타겟이 중간값보다 작으면,
            return binary_search(arr,start,middle-1,t)   # end를 middle -1로
        elif arr[middle] == t:   # 같으면 1반환
            return 1
    else:   # 범위를 벗어나면,
        return 0   # 0반환
import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
t = list(map(int,sys.stdin.readline().split()))

sorted_arr = sorted(arr)   # sort 함수 직접 정의했을 때, 시간초과 상의 이유로

for x in t:
    print(binary_search(sorted_arr,0,N-1,x))   # end는 N-1로