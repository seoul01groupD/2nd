############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 min, max, sorted 함수 리스트 메서드 sort 를 사용하지 않습니다.
def population_difference(population_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    minimum=population_list[0] # 인구 수가 가장 적은 마을의 인구수
    maximum=population_list[0] # 인구 수가 가장 많은 사람의 인구수
    for town in population_list:
        if minimum>town:
            minimum=town
        if maximum<town:
            maximum=town
    return maximum-minimum

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(population_difference([100, 200, 300, 400, 500]))  # 400
print(population_difference([50, 150, 250]))  # 200
print(population_difference([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))  # 90
#####################################################
