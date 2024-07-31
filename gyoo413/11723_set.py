import sys
input = sys.stdin.readline

n = int(input())


class MySet():

    S = set()

    def __init__(self):
        pass

    def add(self, x):
        self.x = x
        if x not in MySet.S:
            MySet.S.add(x)
        return MySet.S

    def remove(self, x):
        self.x = x
        if x in MySet.S:
            MySet.S.remove(x)
        return MySet.S

    def check(self, x):
        self.x = x
        if x in MySet.S:
            print(1)
        else:
            print(0)
        return MySet.S
    
    def toggle(self, x):
        self.x = x
        if x in MySet.S:
            MySet.S.remove(x)
        else:
            MySet.S.add(x)
        return MySet.S
    
    def all(self):
        MySet.S = set(range(1, 21))
        return MySet.S
    
    def empty(self):
        MySet.S = set()
        return MySet.S
    

for i in range(n):
    operation = list(input().strip().split())
    order = operation[0]
    if len(operation) == 2:
        param = int(operation[1])
    S = MySet()
    
    if order == 'add':
        S.add(param)
    elif order == 'remove':
        S.remove(param)
    elif order == 'check':
        S.check(param)
    elif order == 'toggle':
        S.toggle(param)
    elif order == 'all':
        S.all()
    elif order == 'empty':
        S.empty()

