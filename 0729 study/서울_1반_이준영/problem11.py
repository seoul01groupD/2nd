############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    n=len(matrix)
    dy=[0,0,0,1,-1]   # dy,dx는 중심을 기준으로 y축으로 dy, x축으로 dx만큼 가는 걸 표현하기 위해 선언함
    dx=[0,1,-1,0,0]
    for i in range(n):
        for j in range(n):
            counting=0
            for k in range(5):   # 앞에서 선언한 dy,dx의 인덱스로 좌표 변화를 나타냄
                ny=i+dy[k]
                nx=j+dx[k]
                if 0<=ny<=n-1 and 0<=nx<=n-1:
                    counting+=matrix[ny][nx]
            if i==0 and j==0:
                maximum=counting
            elif maximum<counting:
                maximum=counting
    return maximum

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
