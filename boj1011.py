import math
t = int(input())

for i in range(t):
  x, y = map(int, input().split())
  d = y-x
  k = math.sqrt(d)
  if d == 1:
    print(1)
  elif int(k)*int(k) == d:
    print(int(k*2)-1)
  else:
    print(int(k*2))