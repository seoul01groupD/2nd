# 15829

L = int(input())
word = input()
H = 0

for i in range(L):
    # 소문자
    if 97<= ord(word[i]) <= 122:
        H += (ord(word[i])-96) * (31 ** i)
    # 대문자
    else:
        H += (ord(word[i])-64) * (31 ** i)
print(H % 1234567891)