def create(a):
    sum_digit=0 
    while True:
        if a==0:
            break
        else:
            sum_digit=sum_digit+a%10
            a=a//10
    return sum_digit        
a=int(input())
check=0
for i in range(a):
    if i+create(i)==a:
        check=1
        print(i)
        break
if check==0:
    print(0)