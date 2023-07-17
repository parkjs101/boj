n = int(input())
arr = []
for i in range(n):
  arr.append(*map(str, input().split()))
vis_1 = [[0 for _ in range(n)] for _ in range(n)]
vis_2 = [[0 for _ in range(n)] for _ in range(n)]

c_1, c_2 = 0, 0
q_1 = []
q_2 = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
  for j in range(n):
    if vis_1[i][j] == 1:
      continue
    q_1.append([i, j])
    vis_1[i][j] = 1
    c_1 += 1
    while q_1:
      cur_x, cur_y = q_1[-1][1], q_1[-1][0]
      q_1.pop()
      for dir in range(4):
        n_x, n_y = cur_x + dx[dir], cur_y + dy[dir]
        if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n:
          continue
        if arr[n_y][n_x] != arr[cur_y][cur_x] or vis_1[n_y][n_x] == 1:
          continue
        vis_1[n_y][n_x] = 1
        q_1.append([n_y, n_x])

for i in range(n):
  for j in range(n):
    if vis_2[i][j] == 1:
      continue
    q_2.append([i, j])
    vis_2[i][j] = 1
    c_2 += 1
    while q_2:
      cur_x, cur_y = q_2[-1][1], q_2[-1][0]
      q_2.pop()
      for dir in range(4):
        n_x, n_y = cur_x + dx[dir], cur_y + dy[dir]
        if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n:
          continue
        if (((arr[n_y][n_x] == 'R' or arr[n_y][n_x] == 'G') and arr[cur_y][cur_x] == 'B') or 
          ((arr[cur_y][cur_x] == 'R' or arr[cur_y][cur_x] == 'G') and arr[n_y][n_x] == 'B') or vis_2[n_y][n_x] == 1):
          continue
        vis_2[n_y][n_x] = 1
        q_2.append([n_y, n_x])

print(c_1, c_2)