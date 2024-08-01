# 30802
N = int(input())

sizes = list(map(int,input().split()))

T,P = map(int,input().split())

s = 0
for size in sizes:
    count = size // T
    remain = size % T 
    if remain > 0:
        count+=1
    s += count

pen_set = N // P
pen_one = N % P

print(s)
print(pen_set, pen_one)