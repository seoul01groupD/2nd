while True:
    a,b,c=map(int,input().split())
    if a+b+c==0:
        break
    a,b,c=max(a,b,c),a+b+c-max(a,b,c)-min(a,b,c),min(a,b,c)
    if a**2==b**2+c**2:
        print("right")
    else:
        print("wrong")