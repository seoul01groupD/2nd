import sys




T = int(sys.stdin.readline())

index_arr = [0] * 10001

for _ in range(T):
    index_arr[int(sys.stdin.readline())] +=1

for i in range(len(index_arr)):
    if index_arr[i] !=0:
        for j in range(index_arr[i]):
            print(i)



