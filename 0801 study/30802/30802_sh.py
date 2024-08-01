N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
shirt = 0
for i in size:
    if i == 0:
        continue
    elif i <= T:
        shirt += 1
    else:
        shirt += i//T
        if i % T != 0:
            shirt +=1




if P== 0:
    PENCILS = 0
    PENCIL = N
else:
    PENCILS = N//P
    PENCIL = N%P



print(shirt)
print(f'{PENCILS} {PENCIL}')







