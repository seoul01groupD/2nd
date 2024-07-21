# 큐(Queue)

큐는 선입선출 방식으로 작동하는 자료구조

즉, 먼저 들어간 데이터가 먼저 나옴

- Enqueue : 큐의 뒤쪽에 데이터를 추가.
- Dequeue : 큐의 앞쪽에서 데이터를 제거

```
from collections import deque
# 큐 생성

queue = deque()

# 데이터 추가 (enqueue)

queue.append('a')
queue.append('b')
queue.append('c')

print("Queue after enqueuing:", queue)

# 데이터 제거 (dequeue)

print("Dequeued element:", queue.popleft())
print("Queue after dequeuing:", queue)
```


또한, queue 모듈의 Queue 클래스를 사용. 이 클래스는 스레드 안전(thread-safe)한 큐를 제공
```
from queue import Queue

# 큐 생성
queue = Queue()

# 데이터 추가 (enqueue)
queue.put('a')
queue.put('b')
queue.put('c')

print("Queue size after enqueuing:", queue.qsize())

# 데이터 제거 (dequeue)
print("Dequeued element:", queue.get())
print("Queue size after dequeuing:", queue.qsize())
```



# 스택 (Stack)

스택은 후입선출 방식으로 작동하는 자료 구조

즉, 나중에 들어간 데이터가 먼저 나옴 

- **Push**: 스택의 맨 위에 데이터를 추가.
- **Pop**: 스택의 맨 위에서 데이터를 제거.

파이썬에서 스택은 보통 리스트(list)를 사용하여 구현

```
 스택 생성
stack = []

# 데이터 추가 (push)
stack.append('a')
stack.append('b')
stack.append('c')

print("Stack after pushing:", stack)

# 데이터 제거 (pop)
print("Popped element:", stack.pop())
print("Stack after popping:", stack)
```