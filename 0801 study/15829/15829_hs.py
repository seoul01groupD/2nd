L = int(input())
alpha_str = input()
M = 1234567891
hash_value = 0
hash_sq = 0

for alpha in alpha_str: # 입력된 문자열의 각 문자에 대해
    hash_value += (ord(alpha) - 96) * 31 ** hash_sq # ord()를 통해 문자를 정수로 변환
    hash_sq += 1
print(hash_value % M)