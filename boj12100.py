n = int(input())
board = []
count = []
for i in range(n):
  board.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def uldr(d, b):
  board = make_new_board(b)
  if d > 0:
    for i in range(d):
      board = rotate_board_right(board)
  
  for j in range(n):
    lock = []
    for i in range(1, n):
      if board[i][j] == 0:
        continue
      else:
        temp_y = i
        while temp_y > 0 and board[temp_y-1][j] == 0:
          temp_y -= 1
          board[temp_y-1][j] = int(board[temp_y][j])
          board[temp_y][j] = 0
          
        if board[i-1][j] == board[i][j] and i-1 not in lock:
          board[i-1][j] = board[i-1][j]*2
          lock.append(i-1)
          board[i][j] = 0
  
  for i in range(n-d):
    board = rotate_board_right(board)
  return board

def rotate_board_right(b):
  new_board = [[0 for _ in range(n)] for _ in range(n)] 
  for i in range(n):
    for j in range(n):
      new_board[j][n-i-1] = int(b[i][j])
  return new_board

def make_new_board(b):
  new_board = [[0 for _ in range(n)] for _ in range(n)] 
  for i in range(n):
    for j in range(n):
      if b[i][j] != 0:
        new_board[i][j] = int(b[i][j])
  return new_board

def backtracking(b, d, k):
  if k == 6:
    v = 0
    for i in range(n):
      for j in range(n):
        if b[i][j] > v:
          v = int(b[i][j])
    count.append(v)
    return
  else:
    if d == None:
      for i in range(4):
        backtracking(b, i, k+1)
        return
    else:
      new_new_board = uldr(d, make_new_board(b))
      for i in range(4):
        backtracking(new_new_board, i, k+1)
      return
      
backtracking(board, None, 0)
print(max(count))