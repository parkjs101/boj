from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([c for c in str(input())])
q1 = deque()
q2 = deque()
arr_j = arr
arr_f = arr
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
        for j in range(m):
            if arr[i][j] == 'J':
                q1.append([i, j])
                arr_j[i][j] = 1

for i in range(n):
        for j in range(m):
            if arr[i][j] == 'F':
                q2.append([i, j])
                arr_f[i][j] = 1
def func1():
    while q1:
        cy, cx = q1[0][0], q1[0][1]
        q1.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if (ny >= n or ny < 0 or nx >= m or nx < 0
                or arr_j[ny][nx] != '.'):
                continue
            else:
                arr_j[ny][nx] = arr_j[cy][cx] + 1
                q1.append([ny, nx])
    return

def func2():
    while q2:
        cy, cx = q2[0][0], q2[0][1]
        q2.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if (ny >= n or ny < 0 or nx >= m or nx < 0
                or arr_f[ny][nx] == 'F' or arr_f[ny][nx] == '#'):
                continue
            else:
                arr_f[ny][nx] = arr_f[cy][cx] + 1
                q2.append([ny, nx])
    return

def func3():
    v = n*m
    flag = []
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if type(arr_j[i][j]) != int:
                    continue
                else:
                    if arr_j[i][j] < arr_f[i][j]:
                        v = min(v, arr_j[i][j])
                        flag.append(True)
                    else:
                        flag.append(False)
    if True in flag:
        return print(v)
    return print('IMPOSSIBLE')

func1()
func2()
func3()
