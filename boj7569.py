from collections import deque

m, n, h = map(int, input().split())

arr = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)] #3차원 배열 선언

for i in range(h):
    for j in range(n):
        arr[i][j] = list(map(int, input().split()))

q = deque() # h, n, m 순서로 저장
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i, j, k]) #z, y, x

def func1(): 
    while q:
        cz, cy, cx = q[0][0], q[0][1], q[0][2] 
        q.popleft()
        for i in range(6):
            nz, ny, nx = cz + dz[i], cy + dy[i], cx + dx[i]
            if (nx >= m or nx < 0 or ny >= n or ny < 0 or nz >= h or nz < 0 or
                arr[nz][ny][nx] != 0):
                continue
            else:
                arr[nz][ny][nx] = arr[cz][cy][cx] + 1
                q.append([nz, ny, nx])
def func2():
    v = 1
    flag = False
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    flag = False
                    return print(-1)
                elif arr[i][j][k] == -1:
                    continue
                else:
                    flag = True
                    v = max(v, arr[i][j][k])
    if flag == False:
        return print(-1)
    return print(v-1)

func1()
func2()


