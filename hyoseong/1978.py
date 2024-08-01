N = int(input())
num_list = list(map(int, input().split()))
prime_num = 0 # 소수의 개수

for num in num_list:
    
    if num == 1 or num == 2: # 1, 2는 따로 계산
        prime_num += num - 1
        continue
    
    # 자기 자신을 제외한 범위
    for other_num in list(range(2, num)) + list(range(num + 1, 1001)):
        
        if num % other_num == 0: # 나머지가 0이면 소수가 아님
            break
    
    else:
        prime_num += 1
        
print(prime_num)