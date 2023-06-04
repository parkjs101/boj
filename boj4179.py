from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([c for c in str(input())])

arr_j = [a[:] for a in arr]
arr_f = [a[:] for a in arr]
print(id(arr_j))
print(id(arr_f))
print(id(arr))
q1 = deque()
q2 = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if arr_j[i][j] == 'J':
            q1.append([i, j])
            arr_j[i][j] = 1
        if arr_f[i][j] == 'F':
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
                or (arr_f[ny][nx] != '.' and arr_f[ny][nx] != 'J')):
                continue
            else:
                arr_f[ny][nx] = arr_f[cy][cx] + 1
                q2.append([ny, nx])
    return

def func3():
    v = n*m
    flag = False
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if type(arr_j[i][j]) == int:
                    if type(arr_f[i][j]) == int:
                        if arr_j[i][j] < arr_f[i][j]:
                            v = min(v, arr_j[i][j])
                            flag = True
                    else:
                        v = min(v, arr_j[i][j])
                        flag = True
    if flag == True:
        return print(v)
    else:
        return print('IMPOSSIBLE')

func1()
func2()
func3()