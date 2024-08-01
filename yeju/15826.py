# 15829
# 50점

L = int(input())
word = input()
H = 0

for i in range(L):
    if 97<= ord(word[i]) <= 122:
        H += (ord(word[i])-96) * (31 ** i)
    else: 
        H += (ord(word[i])-64) * (31 ** i)
print(H)