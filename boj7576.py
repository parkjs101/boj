from collections import deque

m, n = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([j, i])
        else:
            continue
        
while q:
    cx, cy = q[0][0], q[0][1]
    q.popleft()
    for k in range(4):
        nx, ny = cx + dx[k], cy + dy[k]
        if (nx >= m or nx < 0 or ny >= n or ny < 0 or 
            arr[ny][nx] != 0):
            continue
        else:
            arr[ny][nx] = arr[cy][cx] + 1
            q.append([nx, ny])

def func1():
    v = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return print(-1)
            elif arr[i][j] > v:
                v = arr[i][j]
    return print(v-1)

func1()
