t = int(input())

for i in range(t):
  s = input()
  left = []
  right = []
  for i in range(len(s)):
    if s[i] ==  '<':
      if len(left) > 0:
        right.append(left.pop())
    elif s[i] == '>':
      if len(right) > 0:
        left.append(right.pop())
    elif s[i] == '-':
      if len(left) > 0:
        left.pop()
    else:
      left.append(s[i])
  
  for i in left:
    print(i,end='')
  for i in range(len(right)):
    print(right[-i-1],end='')
  print()