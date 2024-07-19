import sys

n = int(sys.stdin.readline())

queue = []

def push(x):
    global queue
    queue.append(x)
    
def pop():
    global queue
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop(0))

def size():
    global queue
    print(len(queue))

def empty():
    global queue
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front():
    global queue
    if len(queue) != 0:
        print(queue[0])
    else:
        print(-1)

def back():
    global queue
    if len(queue) != 0:
        print(queue[-1])
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
    elif statement == 'front':
        front()
    elif statement == 'back':
        back()
    else:
        state, x = statement.split()
        push(x)