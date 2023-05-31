from collections import deque
n , m = map(int, input().split())
arr = []
visited = [[0]*m for i in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
count = 0
area = 0


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 or visited[i][j] == 1:
            continue
        else:
            visited[i][j] = 1
            count += 1
            cur_area = 1

            queue.append([j, i])
            while queue:
                cx, cy = queue[0][0], queue[0][1]
                queue.popleft()
                for k in range(4):
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    if (nx >= m or nx < 0 or ny >= n or ny <0 or 
                    arr[ny][nx] == 0 or visited[ny][nx] == 1):
                        continue
                    else:
                        queue.append([nx, ny])
                        visited[ny][nx] = 1
                        cur_area += 1
            area = max(area, cur_area)

print(count)
print(area)