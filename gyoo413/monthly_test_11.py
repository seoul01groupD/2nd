############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    n = len(matrix)
    maximum = matrix[0][0]
                        
    for i in range(n):
        for j in range(n):

            dx = [0, 1, -1, 0, 0]
            dy = [0, 0, 0, 1, -1]

            cnt = 0
            for k in range(5):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < n:
                    cnt += matrix[nx][ny]

            if cnt > maximum:
                maximum = cnt

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