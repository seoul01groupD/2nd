n = int(input())
time = list(map(int, input().split()))

maximum = max(time)
sort_time = sorted(time)

for i in range(1, len(sort_time)):
    sort_time[i] += sort_time[i - 1]

print(sum(sort_time))