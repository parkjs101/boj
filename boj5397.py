t = int(input())

for i in range(t):
  s = input()
  p = 0
  arr = ''
  for i in range(len(s)):
    if s[i] == '<':
      if p >0:
        p -= 1
    elif s[i] == '>':
      if p < len(s):
        p += 1
    elif s[i] == '-':
      if p == len(s):
        arr = arr[:p-2]
        p -= 1
      elif p > 0:
        arr = arr[:p-2]+arr[p:]
        p -= 1
    else:
      if p == len(s):
        arr = arr+s[i]
        p += 1
      elif p > 0:
        arr = arr[p-1] + s[i] + arr[p:]
        p += 1
      else:
        arr = s[i]+arr
        p += 1
  
  print(arr)