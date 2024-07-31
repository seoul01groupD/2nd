############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    maximum=0
    longest_str=""
    for string in str_list:
        len_count=0
        for i in string:
            len_count+=1
        if len_count>maximum:
            maximum=len_count  # 이 때까지 최대 길이보다 큰 경우에만 재할당
            longest_str=string # 길이가 같은 문자열이 여러 개여도 큰 경우에만 변수가 바뀌기 때문에 리스트에서 먼저 찾은 길이가 가장 긴 문자열이 반환됨
    return longest_str

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"
