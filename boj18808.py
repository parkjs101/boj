n, m, k = map(int, input().split()) # k = 스티커 개수

board = [[0 for _ in range(m)] for _ in range(n)]
sticker = [0]*k #스티커 정보 저장
count = 0

for l in range(k):
  sticker_n, sticker_m = map(int, input().split())
  sticker[l] = [0 for _ in range(sticker_n)]
  for i in range(sticker_n):
    sticker[l][i] = (list(map(int, input().split())))

def rotate_sticker(l):
  new_sticker = [[0 for _ in range(len(sticker[l]))] for _ in range(len(sticker[l][0]))]
  for i in range(len(sticker[l])):
    for j in range(len(sticker[l][0])):
      new_sticker[j][len(sticker[l])-i-1] = sticker[l][i][j]
  sticker[l] = new_sticker

for l in range(k): #스티커 개수
  for _ in range(4): #방향
    b_flag = False #보드
    for i in range(n-len(sticker[l])+1):
      for j in range(m-len(sticker[l][0])+1):
        s_flag = True #스티커
        is_sticked = False
        new_board = [item[:] for item in board]
        for o in range(len(sticker[l])): 
          for p in range(len(sticker[l][0])):
            if sticker[l][o][p] == 0:
              continue
            elif sticker[l][o][p] == 1 and new_board[i+o][j+p] != 0:
              s_flag = False
              break
            elif sticker[l][o][p] == 1 and new_board[i+o][j+p] == 0:
              new_board[i+o][j+p] = l+1
              is_sticked = True
          if s_flag == False:
            break
        if s_flag == True:
          board = new_board
          b_flag = True
          break
 
      if b_flag == True:
        break
    if b_flag == True:
      break
    else:
      rotate_sticker(l)

for i in range(n):
  for j in range(m):
    if board[i][j] != 0:
      count += 1

print(count)