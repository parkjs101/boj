n, m, k = map(int, input().split()) # k = 스티커 개수

board = [[0 for _ in range(m)] for _ in range(n)]
sticker = [0]*k #스티커 정보 저장

for l in range(k):
  sticker_n, sticker_m = map(int, input().split())
  sticker[l] = [0 for _ in range(sticker_n)]
  for i in range(sticker_n):
    sticker[l][i] = (list(map(int, input().split())))

print(sticker)

for l in range(k):
  cur_sticker = sticker[l]
  for _ in range(4):
    for i in range(n):
      for j in range(m):
        cur_x = 0
        cur_y = 0
        while True:
          if cur_sticker[cur_y][cur_x] == 0 and sticker[n+cur_y][m+cur_x] == 0:
            pass
          elif cur_sticker[cur_y][cur_x] == 1 and sticker[n+cur_y][m+cur_x] == 0:
            pass
          elif cur_sticker[cur_y][cur_x] == 1 and sticker[n+cur_y][m+cur_x] == 1:
            flag = False
            break
          elif cur_sticker[cur_y][cur_x] == 0 and sticker[n+cur_y][m+cur_x] == 1:
            flag = False
            break