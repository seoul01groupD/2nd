a = int(input())

temp_list = []
for i in range(a):
    b= a-i
    c = list(map(int, str(b)))
    if b + sum(c) == a:
        temp_list.append(b)
        
if temp_list == []:
    print("0")
else:
            
    print(min(temp_list))
    
        
        
        
       
    # print(min(temp_list))
        



