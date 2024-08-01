def quick_pow(a,b): #  a**b계산
    result=1
    while b>0:
        if b%2==1:
            result*=a 
        a=a*a
        b=b//2
    return result