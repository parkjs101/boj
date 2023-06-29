n = int(input())
board = []
count = -1
for i in range(n):
  board.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def uldr(d, b):
  board = make_new_board(b)
  
  for i in range(d%4):
    board = rotate_board_right(board)
  
  for j in range(n):
    lock = [0]*(n+2)
    for i in range(1, n):
      if board[i][j] == 0:
        continue
      else:
        temp_y = i
        while temp_y > 0 and board[temp_y-1][j] == 0:
          board[temp_y-1][j] = board[temp_y][j]
          board[temp_y][j] = 0
          temp_y -= 1
          
        if temp_y > 0 and board[temp_y][j] == board[temp_y-1][j] and lock[temp_y-1] == 0:
          board[temp_y-1][j] = board[temp_y-1][j]*2
          lock[temp_y-1] = 1
          board[temp_y][j] = 0

  for i in range((n-d)%4):
    board = rotate_board_right(board)
  return board

def rotate_board_right(board):
  new_board = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      new_board[j][n-i-1] = board[i][j]
  return new_board

def make_new_board(b):
  new_board = [[0 for _ in range(n)] for _ in range(n)] 
  for i in range(n):
    for j in range(n):
      new_board[i][j] = b[i][j]
  return new_board

def backtracking(board, d, k):
  global count
  if k == 5:
    for i in range(n):
      for j in range(n):
        if board[i][j] > count:
          count = board[i][j]
    return
  elif k < 5:
    new_new_board = uldr(d, board)
    if k < 4:
      for i in range(4):
        backtracking(new_new_board, i, k+1)
    if k == 4:
      backtracking(new_new_board, None, k+1)
    return

for i in range(4):
  backtracking(board, i, 0)
print(count)