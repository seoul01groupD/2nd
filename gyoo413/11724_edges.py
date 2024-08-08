v, e = map(int, input().split())
lst = []
for i in range(e):
    lst.extend(list(map(int, input().split())))
adjL = [[] for _ in range(v + 1)]
for i in range(e):
    v1, v2 = lst[2*i], lst[2*i + 1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)


def DFS(s, n):
    visited = [0] * (n + 1)
    stack = []
    v = s
    cnt = 0
    for i in range(s, len(visited)):
        if visited[i] == 0:
            v = i
            while True:
                for w in adjL[v]:
                    if not visited[w]:
                        visited[w] = 1
                        stack.append(v)
                        v = w
                        break
                else:
                    if stack:
                        v = stack.pop()
                    else:
                        break
            cnt += 1

    return cnt


print(DFS(1, v))

