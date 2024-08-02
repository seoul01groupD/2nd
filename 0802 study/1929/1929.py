m,n=map(int,input().split())
end=1000001
arr=[True]*end
arr[0]=False
arr[1]=False
for i in range(2,int(end**(1/2))+1):
    if not arr[i]:
        continue
    else:
        for j in range(i*i,end,i):
            arr[j]=False
for i in range(m,n+1):
    if arr[i]==True:
        print(i)