n=map(int,input().split())
numbers=list(map(int,input().split()))
end=1001
arr=[True]*end
arr[0]=False
arr[1]=False
for i in range(2,int(end**(1/2))+1):
    if not arr[i]:
        continue
    else:
        for j in range(i*i,end,i):
            arr[j]=False
count=0
for num in numbers:
    if arr[num]:
        count+=1
print(count)