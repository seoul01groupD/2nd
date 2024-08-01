import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
t,p=map(int,input().split())
count=0
for i in arr:
    count=count+1+(i-1)//t
print(count)
print(n//p,n%p)