n, m = map(int, input().split())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

chicken = []
house = []
dis = []

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      house.append([i, j])
    elif arr[i][j] == 2:
      chicken.append([i, j])
      
is_used = [0]*len(chicken)

def backtracking(k, value):
  if k > 0 and k <= m:
    d = 0
    for h in house:
      temp = 2*n
      for i in range(len(chicken)):
        if is_used[i] == 1:
          v = distance(h[0], chicken[i][0], h[1], chicken[i][1])
          if v < temp:
            temp = v
      d += temp
    dis.append(d)
    
    for i in range(value, len(chicken)):
      if is_used[i] == 0:
        is_used[i] = 1
        backtracking(k+1, i)
        is_used[i] = 0 
    return
  elif k == 0:
    for i in range(len(chicken)):
      is_used[i] = 1
      backtracking(1, i)
      is_used[i] = 0
    return
  
  else:
    return

def distance(x1, x2, y1, y2):
  if x1 > x2:
    dx = x1 - x2
  else:
    dx = x2 - x1
  if y1 > y2:
    dy = y1 - y2
  else:
    dy = y2 - y1
  return dx+dy

backtracking(0, None)

print(min(dis))