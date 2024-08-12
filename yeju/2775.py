# 2775

T = int(input())
for tc in range(1,T+1):
    k = int(input())   # 층
    n = int(input())   # 호
    fn = [[i for i in range(1,n+1)]]   # 주민의 수를 나타내는 2차원 배열

    # k층 n호에 사는 주민의 수
    for i in range(k):
        a = []   # i층에 있는 n개의 호의 주민
        fs = 0   # 호수별 인원
        for j in range(n):
            fs += fn[i][j]   # k-1층의 n호까지의 주민의 합
            a.append(fs)
        fn.append(a)

    result = fn[k][n-1]   # k층 n호의 주민
    print(result)