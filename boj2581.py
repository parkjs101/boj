M = int(input())
N = int(input())
li = []
for i in range(M, N+1):
  flag = True
  if i == 1:
    flag = False
    continue
  for j in range(2, i//2+1):
    if i%j == 0:
      flag = False
      break
  if flag == True:
    li.append(i)

if len(li) > 0:
  print(sum(li))
  print(li[0])
else:
  print(-1)