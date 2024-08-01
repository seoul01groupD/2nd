M, N = map(int, input().split())
# 0, 1은 False, 나머지는 True인 0부터 N까지의 배열 생성
prime = [False, False] + [True] * (N - 1)
p = 2 # 첫 소수인 2부터 시작

while p <= N ** (1 / 2): # 루트 N보다 p가 작을 때
    if prime[p]:
        # 배열에서 p의 배수 부분은 Fasle로 설정
        for i in range(p * p, N + 1, p):
            prime[i] = False
    p += 1

# M부터 N 범위 내의 수에 대해 True면 소수
for q in range(M, N + 1):
    if prime[q]:
        print(q)