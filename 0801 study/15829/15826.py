l=int(input())
c=input()
a=0
for i in range(l):
    a=a+(ord(c[i])-ord("a")+1)*31**i
print(a%1234567891)