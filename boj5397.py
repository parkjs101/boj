from collections import deque

t = int(input())

for i in range(t):
  s = input()
  p = 0
  arr = deque()
  for i in range(len(s)):
    if s[i] == '<':
      if p > 0:
        p -= 1
    elif s[i] == '>':
      if p < len(arr):
        p += 1
    elif s[i] == '-':
      if p == len(arr) and len(arr)>0:
        arr.pop()
        p -= 1
      elif p > 0:
        newarr = deque()
        for j in range(len(arr)+1):
          if j < p-1:
            newarr.append(arr.popleft())
          elif j == p-1:
            arr.popleft()
          if j > p-1:
            newarr.append(arr.popleft())
        arr = newarr
        p -= 1
    else:
      if p == len(arr):
        arr.append(s[i])
        p += 1
      elif p > 0:
        newarr = deque()
        for j in range(len(arr)+1):
          if j < p:
            newarr.append(arr.popleft())
          elif j == p:
            newarr.append(s[i])
          if j > p:
            newarr.append(arr.popleft())
        arr = newarr
        p += 1
      else:
        arr.appendleft(s[i])
        p += 1

  for i in range(len(arr)):
    if i == len(arr)-1:
      print(arr[i])
    else:
      print(arr[i],end='')