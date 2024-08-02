# 1978

N = int(input())
nums = list(map(int,input().split()))

prime_num = []
for num in nums:
    if num > 1: 
        p = 0
        for i in range(2,num+1):
            if num % i == 0:
                p += 1
        if p == 1:
            prime_num.append(num)

print(len(prime_num))