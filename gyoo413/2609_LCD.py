a, b = map(int, input().split())

def find_divisor(a, b):
    big = small = 1

    if a > b:
        big = a
        small = b
    elif a < b:
        big = b
        small = a
    else:
        return a

    if big % small == 0:
        return small
    else:
        return find_divisor(small, big % small)
    
    

common_divisor = find_divisor(a, b)
print(common_divisor)

common_multiplier = common_divisor * (a // common_divisor) * (b // common_divisor)
print(common_multiplier)