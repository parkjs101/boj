n, m = map(int, input().split())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))
cctv = []
xy = []
count = 0
for i in range(n):
    for j in range(m):
        if li[i][j] == 0 or li[i][j] == '#' or li[i][j] == 6:
            pass
        elif li[i][j] == 1 or li[i][j] == 3 or li[i][j] == 4:
            cctv.append([li[i][j], 4])
            xy.append([i, j])
        elif li[i][j] == 2:
            cctv.append([li[i][j], 2])
            xy.append([i, j])
        elif li[i][j] == 5:
            cctv.append([li[i][j], 1])
            xy.append([i, j])

cctv_count = [0 for _ in range(len(cctv))]

while True:
    board = li

    for i in range(xy):
        cur_y = xy[i][0]
        cur_x = xy[i][1]
        if cctv[i][0] == '1':
            if cctv_count[i]%4 == 0:
                while board[cur_y, cur_x] != '6' or cur_x >= m or cur_x < 0 or cur_y >= n or cur_y < 0:
                    cur_x = cur_x+1
                    board[cur_y, cur_x] = '#'
                cctv_count[i] += 1
            elif cctv_count[i]%4 == 1:
                while board[cur_y, cur_x] != '6' or cur_x >= m or cur_x < 0 or cur_y >= n or cur_y < 0:
                    cur_y = cur_y+1
                    board[cur_y, cur_x] = '#'
                cctv_count[i] += 1
            elif cctv_count[i]%4 == 2:
                while board[cur_y, cur_x] != '6' or cur_x >= m or cur_x < 0 or cur_y >= n or cur_y < 0:
                    cur_x = cur_x-1
                    board[cur_y, cur_x] = '#'
                cctv_count[i] += 1
            elif cctv_count[i]%4 == 3:
                while board[cur_y, cur_x] != '6' or cur_x >= m or cur_x < 0 or cur_y >= n or cur_y < 0:
                    cur_y = cur_y-1
                    board[cur_y, cur_x] = '#'

        elif cctv[i][0] == '2':
            if cctv_count[i]%2 == 0:
                while board[cur_y, cur_x] != '6' or cur_x >= m or cur_x < 0 or cur_y >= n or cur_y < 0:
                    cur_x = cur_x+1
                    board[cur_y, cur_x] = '#'
                cur_x = xy[i][1]
                while board[cur_y, cur_x] != '6' or cur_x >= m or cur_x < 0 or cur_y >= n or cur_y < 0:
                    cur_x = cur_x-1
                    board[cur_y, cur_x] = '#'
                cctv_count[i] += 1
            elif cctv_count[i]%2 == 1:
                while board[cur_y, cur_x] != '6' or cur_x >= m or cur_x < 0 or cur_y >= n or cur_y < 0:
                    cur_y = cur_y+1
                    board[cur_y, cur_x] = '#'
                cur_y = xy[i][0]
                while board[cur_y, cur_x] != '6' or cur_x >= m or cur_x < 0 or cur_y >= n or cur_y < 0:
                    cur_y = cur_y-1
                    board[cur_y, cur_x] = '#'
                cctv_count[i] += 1