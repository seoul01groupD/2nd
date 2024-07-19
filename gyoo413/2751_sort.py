import sys

n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    def sorting(left, right):
        i = j = 0
        sorted_list = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
            
        while i < len(left):
            sorted_list.append(left[i])
            i += 1

        while j < len(right):
            sorted_list.append(right[j])
            j += 1

        return sorted_list

    left_ = merge_sort(left)
    right_ = merge_sort(right)

    return sorting(left_, right_)

num_list = merge_sort(num_list)

for num in num_list:
    print(num)