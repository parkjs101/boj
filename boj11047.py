n, k = map(int, input().split())
arr = []
for i in range(n):
  arr.append(int(input()))
count = 0
i = -1
while True:
  if k >= arr[i]:
    count += k//arr[i]
    k = k%arr[i]
  i -= 1
  if k == 0:
    break

print(count)