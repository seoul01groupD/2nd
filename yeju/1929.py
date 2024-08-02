# 1929
# power 써서 구현해야될듯

m,n = map(int,input().split())

prime_num = []
for num in range(m,n+1):
    if num > 1:
        count = 0
        for i in range(2,num+1):
            if num % i == 0:
                count += 1

        if count == 1:
            print(num)