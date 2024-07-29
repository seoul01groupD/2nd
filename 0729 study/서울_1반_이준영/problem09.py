############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_number_sum(word):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    counting=0 # 숫자들의 합
    ch=["0"]  # 연속한 숫자들을 표현하기 위한 임시 리스트
    length=len(word)
    for i in range(length):
        if word[i].isdigit():   # 요소가 숫자이면 ch에 추가하고, 아니면 지금까지 ch에 저장된 문자열을 모두 합쳐 int로 변환 후 더함
            ch.append(word[i])
        else:
            counting+=int("".join(ch))
            ch=["0"]
        if i==length-1:
            counting+=int("".join(ch))
    return counting    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_number_sum('ab123cd45ef6'))     # 174
print(calculate_number_sum('0a1s2d3f4'))        # 10
print(calculate_number_sum('ssafy10gi2good4560')) # 4572
#####################################################
