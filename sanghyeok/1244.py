T = int(input())

arr = list(map(int, input().split()))

students = int(input())

for i in range(students):
    s, n = map(int, input().split())
    if s == 1:
        for i in range(n,T+1,n):
            if arr[i-1] == 1:
                arr[i-1] = 0
            else:
                arr[i-1] = 1


    elif s == 2:
        for a in range(1, n):
            if 0<=n-1-a and n-1+a < T and arr[n-1-a] == arr[n-1+a]:
                if arr[n-1-a] and arr[n-1+a] == 1:
                    arr[n - 1 - a] = 0
                    arr[n - 1 + a] = 0
                else:
                    arr[n - 1 - a] = 1
                    arr[n - 1 + a] = 1
        if arr[n - 1] == 1:
            arr[n-1] = 0
        else:
            arr[n-1] = 1

for i in range(0, T, 20):
    print(" ".join(map(str, arr[i:i+20])))
