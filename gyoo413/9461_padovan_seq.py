T = int(input())

padovan = [1, 1, 1, 2, 2]
for i in range(5, 100):
    padovan.append(padovan[i - 1] + padovan[i - 5])

for i in range(T):
    n = int(input())
    print(padovan[n - 1])
        