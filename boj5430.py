from collections import deque

t = int(input())

def discard(li, key):
  if key == 1:
    li.popleft()
  elif key == 0:
    li.pop()

for i in range(t):
  p = input()
  n = int(input())

  if n == 0:
    a = input()
    s = deque()
  else:
    s = deque(list(map(int, input().strip('[]').split(','))))

  flag = 1
  key = 1

  for j in range(len(p)):
    if p[j] == 'R':
      key += 1
      key = key%2

    elif p[j] == 'D':
      if len(s) == 0:
        flag = -1
        break
      discard(s, key)

  if key == 0:
    s.reverse()

  if flag != -1 and len(s) == 0:
    flag = 2

  if flag == -1:
    print('error')
  elif flag == 2:
    print('[]')
  else:
    print(str(s).strip('deque()').replace(" ",""))