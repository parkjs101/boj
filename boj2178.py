from collections import deque
n , m = map(int, input().split())

arr = []
visited = [[0]*m for i in range(n)]

for i in range(n):
    arr.append(list(str(input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()
cx, cy = 0, 0
visited[0][0] = 1
q.append([0, 0])

while q:
    cx, cy = q[0][0], q[0][1]
    q.popleft()

    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if (nx >= m or nx < 0 or ny >= n or ny < 0 or arr[ny][nx] == '0' or visited[ny][nx] != 0):
            continue
        else:
            visited[ny][nx] = visited[cy][cx] + 1
            q.append([nx, ny])

print(visited[n-1][m-1])

