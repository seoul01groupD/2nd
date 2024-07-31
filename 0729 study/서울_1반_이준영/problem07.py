############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_days_to_fill_tank(tank_capacity, fill_amount, evaporation_amount):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    counting=1 # 걸리는 일수
    amount=0 # 현재 물탱크의 물의 양
    while True:
        amount+=fill_amount
        if amount>=tank_capacity:  # 낮에 넣어서 물탱크 다 채운 경우
            break
        amount-=evaporation_amount # 물이 증발함
        counting+=1 # 하루가 지남
    return counting


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_days_to_fill_tank(100, 20, 5))  # 7
print(calculate_days_to_fill_tank(1000, 100, 10))  # 11
print(calculate_days_to_fill_tank(100, 10, 1))  # 11
#####################################################
