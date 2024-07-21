# 머지 소트(Merge sort)

머지 소트는 효율적이고 안정적인 정렬 알고리즘

분할 정복 전략을 사용

주어진 배열을 반으로 나누어 각각을 재귀적으로 정렬한 후, 두 개의 정렬된 배열을 병합하여 전체 배열을 정렬함

### 머지 소트 작동 원리

1. **분할 (Divide)**: 배열을 반으로 나눔
2. **정복 (Conquer)**: 각 부분 배열을 재귀적으로 정렬
3. **병합 (Merge)**: 두 개의 정렬된 부분 배열을 하나의 정렬된 배열로 합침

```
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 배열을 두 부분으로 분할
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 분할한 부분 배열을 재귀적으로 정렬
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # 두 개의 정렬된 부분 배열을 병합
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    # 두 배열을 비교하며 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # 남은 요소들을 추가
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# 사용 예제
unsorted_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(unsorted_array)
print("Sorted array:", sorted_array)
```
결과
```
Sorted array: [3, 9, 10, 27, 38, 43, 82]
```

### 설명

1. `merge_sort` 함수는 배열이 1개 이하의 요소를 갖고 있으면 그대로 반환하고, 그렇지 않으면 배열을 반으로 나눕니다.
2. 배열이 반으로 나뉘어질 때까지 재귀적으로 `merge_sort`를 호출합니다.
3. `merge` 함수는 두 개의 정렬된 배열을 병합하여 하나의 정렬된 배열로 만듭니다. 두 배열의 첫 요소를 비교하여 작은 요소를 결과 배열에 추가하고, 그 배열의 인덱스를 증가시킵니다.
4. 한 배열이 모두 결과 배열에 추가되면 나머지 배열의 모든 요소를 결과 배열에 추가합니다.


### 개인적인 생각
1. [38, 27, 43, 3, 9, 82, 10] 값이 있었을 때 반으로 나누고 나눠서 정렬함(오름차순)
2. 예시 [38, 27, 43], [3,9,82,10]
3. 또 다시 반을 가르고 병합함
4. ex) [3,9],[82,10] -> [3], [9], [82], [10] -> [3,9,10,82]
5. 반복하여 [3,9,10,27,38,82]를 만듬
