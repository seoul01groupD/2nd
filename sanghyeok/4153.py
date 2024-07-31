def my_max(arr):
    max_value = arr[0]
    for i in arr:
        if max_value<i:
            max_value = i
            
    return max_value



while True:
    H,A1,A2 = map(int, input().split())
    arr = [H,A1,A2]
    if arr[0]==0 and arr[1]==0 and arr[2] ==0:
        break
    if my_max(arr) == H:
        if H**2 == A1**2+A2**2:
            print('right')
        else:
            print('wrong')
    elif my_max(arr)==A1:
        if A1**2 == H**2 + A2**2:
            print('right')
        else:
            print('wrong')
    elif my_max(arr) == A2:
        if A2**2 == H**2 + A1**2:
            print('right')
        else:
            print('wrong')
    
    
    
  



