n = int(input())
li = []
arr = []
value = [0,0]
m = n*(n-1)//2
isused = [0]*(n+1)


for i in range(n):
  li.append(list(map(int, input().split())))

for i in range(1, n+1):
  for j in range(1, n+1):
    if i >= j:
        continue
    arr.append([i, j])

print(arr)