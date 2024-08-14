# 10814 ---> 시간 초과
N = int(input())
arr = [list(input().split()) for _ in range(N)]

# 버블 정렬
for i in range(N-1,0,-1):
    for j in range(i):
        if int(arr[j][0]) > int(arr[j+1][0]):   # 같거나 크면 그냥 pass
            arr[j], arr[j+1] = arr[j+1], arr[j]

# # 퀵 정렬
# def quick_sort(a,begin,end):
#     if begin < end:
#         p = partition(a,begin,end)
#         quick_sort(a,begin,p-1)
#         quick_sort(a,p+1,end)
#
# def partition(a,begin,end):
#     pivot = (begin + end) // 2
#     L = begin
#     R = end
#     while L < R:
#         while L < R and int(a[L][0]) < int(a[pivot][0]):
#             L += 1
#         while L < R and int(a[R][0]) >= int(a[pivot][0]):
#             R -= 1
#         if L < R:
#             if L == pivot:
#                 pivot = R
#             a[L],a[R] = a[R],a[L]
#     a[pivot],a[R] = a[R],a[pivot]
#     return R
#
# arr_1 = quick_sort(arr,0,N-1)
# print(arr_1)

# 결과값 출력
for x in arr:
    print(*x)