import sys
def mid(arr):
    mid_value2 = len(arr)//2

    return arr[mid_value2]

def mode(arr):
    if abs(max(arr)) < abs(min(arr)):
        mode_n = abs(min(arr))
        count = [0] * (2*mode_n + 1)
        for i in arr:
            if i >=0:
                count[2*i] += 1
            else:
                count[-i] += 1


    else:
        mode_n = abs(max(arr))
        count = [0] * (mode_n + 1)
        for i in arr:
            count[i] += 1
    m = 0
    for j in count:
        if j == max(count):
            m +=1
    if m > 1:
        max_count = max(count)
        mode_values = []

        for i, c in enumerate(count):
            if c == max_count:
                if i % 2 == 0:
                    mode_values.append(i//2)
                else:
                    mode_values.append(-i)

        return count.index(max(count))
    else:  # 최빈값이 1개이면 해당 숫자를 리턴
        return count.index(max(count))





def average(arr):
    sum_value = sum(arr)
    average_value = int(sum_value / len(arr))
    average_value2 = str(average_value*10)
    if int(average_value2[-1]) >= 5:
        return average_value == average_value + 1
    else:
        return average_value




T = int(sys.stdin.readline())

temp = []

for i in range(T):
    N = int(sys.stdin.readline())
    temp.append(N)




sort_temp = sorted(temp)
mid_value = mid(sort_temp)
scope = max(temp) - min(temp)


print(average(temp))
print(mid_value)
print(mode(temp))
print(scope)