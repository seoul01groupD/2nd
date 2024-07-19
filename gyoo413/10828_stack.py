import sys

n = int(sys.stdin.readline())

stack = []

def push(x):
    global stack
    stack.append(x)
    
def pop():
    global stack
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop() 

def size():
    global stack
    print(len(stack))

def empty():
    global stack
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    global stack
    if len(stack) != 0:
        print(stack[-1])
    else:
        print(-1)


for i in range(n):
    statement = sys.stdin.readline().rstrip()

    if statement == 'pop':
        pop()
    elif statement == 'size':
        size()
    elif statement == 'empty':
        empty()
    elif statement == 'top':
        top()
    else:
        state, x = statement.split()
        push(x)