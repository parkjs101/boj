#2023.07.04 15:57
from collections import deque
n = int(input())
arr = []
dist = []

for i in range(n):
  arr.append(list(map(int, input().split())))
  
dy = [1, 0, 0, -1]  
dx = [0, -1, 1, 0]
queue = deque()
baby = 2
levelup_stack = 0
time = 0
visited = []


for i in range(n):
  for j in range(n):
    if arr[i][j] == 9:
      queue.append([i, j])
      visited.append([i, j])
      arr[i][j] = 0

dist =  [[0 for _ in range(n)] for _ in range(n)]

while queue:
  cy = queue[0][0]
  cx = queue[0][1]
  queue.popleft()

  for i in range(4):
    y = cy + dy[i]
    x = cx + dx[i]
    if y >= n or y < 0 or x >= n or x < 0:
      continue
    elif arr[y][x] > baby or [y, x] in visited:
      continue
    
    elif arr[y][x] == baby or arr[y][x] == 0:
      queue.append([y, x])
      visited.append([y, x])
      dist[y][x] = dist[cy][cx] + 1
    
    elif arr[y][x] < baby:
      queue = deque([[y, x]])
      visited = [[y, x]]
      arr[y][x] = 0

      levelup_stack += 1
      if levelup_stack == baby:
        baby += 1
        levelup_stack = 0
      print(dist[cy][cx])
      time += dist[cy][cx] + 1
      
      print(time)
      print(dist)
      
      dist = [[0 for _ in range(n)] for _ in range(n)]
      

print(time)
  