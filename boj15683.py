n, m = map(int, input().split())
arr = []
cctv = []
count = []
v = 0
for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if arr[i][j] != 6 and arr[i][j] != 0:
            v += 1
            cctv.append([arr[i][j], i, j])
        elif arr[i][j] == 6:
            v += 1

def count_backtracking(k, array, v):
    if k == len(cctv):
        count.append(n*m-v)
        return
    else:
        if cctv[k][0] == 1:
            rotate_cctv1(k, array, v)
        elif cctv[k][0] == 2:
            rotate_cctv2(k, array, v)
        elif cctv[k][0] == 3:
            rotate_cctv3(k, array, v)
        elif cctv[k][0] == 4:
            rotate_cctv4(k, array, v)
        elif cctv[k][0] == 5:
            rotate_cctv5(k, array, v)


def rotate_cctv1(k, array, v):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cx = cctv[k][2]
    cy = cctv[k][1]
    for i in range(4):
        temp = 0
        nx = cx 
        ny = cy
        while nx >= 0 and nx < m and ny >= 0 and ny < n and array[ny][nx] != 6:
            if array[ny][nx] == 0:
                temp += 1
                array[ny][nx] = 10+k
            nx = nx+dx[i]
            ny = ny+dy[i]
        v += temp
        count_backtracking(k+1, array, v)
        v -= temp
        for i in range(n):
            for j in range(m):
                if array[i][j] == 10+k:
                    arr[i][j] = 0
    return 

def rotate_cctv2(k, array, v):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cx = cctv[k][2]
    cy = cctv[k][1]
    for i in range(4):
        if i%2 == 0:
            temp = 0
        nx = cx 
        ny = cy
        while nx >= 0 and nx < m and ny >= 0 and ny < n and array[ny][nx] != 6:
            if array[ny][nx] == 0:
                temp += 1
                array[ny][nx] = 20+k
            nx = nx+dx[i]
            ny = ny+dy[i]
        if i%2 == 1:
            v += temp
            count_backtracking(k+1, array, v)
            v -= temp
        for i in range(n):
            for j in range(m):
                if array[i][j] == 20+k:
                    arr[i][j] = 0
    return 

def rotate_cctv3(k, array, v):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cx = cctv[k][2]
    cy = cctv[k][1]
    for i in range(4):
        temp = 0
        for j in range(2):
            nx = cx 
            ny = cy
            while nx >= 0 and nx < m and ny >= 0 and ny < n and array[ny][nx] != 6:
                if array[ny][nx] == 0:
                    temp += 1
                    array[ny][nx] = 30+k
                if j == 0:
                    nx = nx+dx[i]
                    ny = ny+dy[i]
                elif j == 1:
                    nx = nx+dx[(i+1)%4]
                    ny = ny+dy[(i+1)%4]
        v += temp
        count_backtracking(k+1, array, v)
        v -= temp
        for i in range(n):
            for j in range(m):
                if array[i][j] == 30+k:
                    arr[i][j] = 0
    return

def rotate_cctv4(k, array, v):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cx = cctv[k][2]
    cy = cctv[k][1]
    for i in range(4):
        temp = 0
        for j in range(3):
            nx = cx 
            ny = cy
            while nx >= 0 and nx < m and ny >= 0 and ny < n and array[ny][nx] != 6:
                if array[ny][nx] == 0:
                    temp += 1
                    array[ny][nx] = 40+k
                if j == 0:
                    nx = nx+dx[i]
                    ny = ny+dy[i]
                elif j == 1:
                    nx = nx+dx[(i+1)%4]
                    ny = ny+dy[(i+1)%4]
                elif j == 2:
                    nx = nx+dx[(i+2)%4]
                    ny = ny+dy[(i+2)%4]
        v += temp
        count_backtracking(k+1, array, v)
        v -= temp
        for i in range(n):
            for j in range(m):
                if array[i][j] == 40+k:
                    arr[i][j] = 0
    return

def rotate_cctv5(k, array, v):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cx = cctv[k][2]
    cy = cctv[k][1]
    temp = 0
    for i in range(4):
        nx = cx 
        ny = cy
        while nx >= 0 and nx < m and ny >= 0 and ny < n and array[ny][nx] != 6:
            if array[ny][nx] == 0:
                temp += 1
                array[ny][nx] = 50+k
            nx = nx+dx[i]
            ny = ny+dy[i]  
    v += temp
    count_backtracking(k+1, array, v)
    v -= temp
    for i in range(n):
            for j in range(m):
                if array[i][j] == 50+k:
                    arr[i][j] = 0
    return

count_backtracking(0, arr, v)
print(min(count))