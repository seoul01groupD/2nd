n = int(input())
lst = []
for i in range(n):
    lst.append(list(input().split()))

for i in range(n):
    lst[i][0] = int(lst[i][0])


def merge_sort(left, right):
        i, j = 0, 0
        sorted_list = []

        while(i < len(left) and j < len(right)):
            if left[i][0] <= right[j][0]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        while(i < len(left)):
            sorted_list.append(left[i])
            i += 1
        while(j < len(right)):
            sorted_list.append(right[j])
            j += 1

        return sorted_list


def merge_sorting(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left_ = merge_sorting(left)
    right_ = merge_sorting(right)

    return merge_sort(left_, right_)


lst = merge_sorting(lst)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end = ' ')
    print('')