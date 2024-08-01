N = int(input())
Size_list = list(map(int,input().split()))
T, P = map(int,input().split())
need_order = 0 # 티셔츠를 T장씩 주문할 때 최소 묶음

for size in Size_list:
    if size != 0: # size가 0인 경우 제외
        if size % T != 0: # size가 T로 딱 떨어지지 않으면
            need_order += size // T + 1 # T로 나눈 몫 + 1
        else:
            need_order += size // T
print(need_order)
print(N // P, N % P) # 펜의 경우 N을 P로 나눈 몫, 나머지 출력