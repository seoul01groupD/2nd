t=int(input())
for tc in range(t):
    h,w,n=map(int,input().split())
    height=(n-1)%h+1
    room=(n-1)//h+1
    print(height*100+room)