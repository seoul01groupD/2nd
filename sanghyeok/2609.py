def max_(a, b):
    arr = [2, 3, 5, 7]
    max_value = 1
    a1 = a
    b1 = b
    for i in arr:
        if a%i == 0 and b%i == 0:
            a1 = a1//i
            b1 = b1//i
            max_value = max_value* i


    return max_value

def min_(a, b):
    arr = [2,3,5,7]
    min_value = 1
    a1 = a
    b1 = b
    for i in arr:
        if a%i == 0 and b%i == 0:
            a1 = a1//i
            b1 = b1//i
            min_value = min_value*i



    return  min_value*a1*b1


a, b = map(int, input().split())

result = max_(a, b)
result2 = min_(a, b)

print(result)
print(result2)