n = int(input())
s = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alpha)

def my_index(x):
    for i in range(len(alpha_list)):
        if alpha_list[i] == x:
            return (i + 1)

ans = 0

for i in range(len(s)):
    ans += my_index(s[i]) * (31 ** i)

ans = ans % 1234567891

print(ans)