import sys

input = sys.stdin.readline
n = int(input())
difficult = []
for i in range(n):
    difficult.append(int(input()))

def my_round(x):
  y = x * 10
  if y % 10 >= 5:
    return int((y // 10) + 1)
  else:
    return int(y // 10)

if n == 0:
    print(0)
else:
    def merge_sort(unsorted_list):

        length=len(unsorted_list)

        if length <= 1:
            return unsorted_list
        
        mid = length // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        i = j = 0
        sorted_list = []
        l = length // 2; r = (length + 1) // 2

        while i < l and j < r:
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        while i < l:
            sorted_list.append(left[i])
            i += 1

        while j < r:
            sorted_list.append(right[j])
            j += 1

        return sorted_list 

    sort_diff = merge_sort(difficult)

    out = my_round(n * 0.15)

    if out != 0:
        sort_diff = sort_diff[out:-out]

    mean = my_round(sum(sort_diff) / len(sort_diff))

    print(mean)