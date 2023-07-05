#2023.07.04 15:57
from collections import deque
n = int(input())
arr = []

for i in range(n):
  arr.append(list(map(int, input().split())))
  
dy = [-1, 0, 0, 1]  
dx = [0, -1, 1, 0]
queue = deque()
baby = 2
levelup_stack = 0
time = 0
visited = []
heap = []

for i in range(n):
  for j in range(n):
    if arr[i][j] == 9:
      queue.append([i, j])
      visited.append([i, j])
      arr[i][j] = 0

dist = [[0 for _ in range(n)] for _ in range(n)]

flag = True
while flag:
  flag = False
  while queue:
    cy, cx = queue[0][0], queue[0][1]
    queue.popleft()
    for i in range(4):
      y, x = cy + dy[i], cx + dx[i]
      if y >= n or y < 0 or x >= n or x < 0:
        continue
      elif arr[y][x] > baby or [y, x] in visited:
        continue
      
      elif arr[y][x] == baby or arr[y][x] == 0:
        queue.append([y, x])
        visited.append([y, x])
        dist[y][x] = dist[cy][cx] + 1
        
      elif arr[y][x] != 0 and arr[y][x] < baby:
        heap.append([dist[cy][cx] + 1, y, x])
        visited.append([y, x])
        dist[y][x] = dist[cy][cx] + 1
        flag = True
        
  if flag == True:
    heap.sort()
    y, x = heap[0][1], heap[0][2]
    heap = []
    arr[y][x] = 0
    queue = deque([[y, x]])
    visited = [[y, x]]
    levelup_stack += 1
    if levelup_stack == baby:
      baby += 1
      levelup_stack = 0
    time += dist[y][x]
    dist = [[0 for _ in range(n)] for _ in range(n)]
      
print(time)
  