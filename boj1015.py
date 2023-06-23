n = int(input())

arr = list(map(int, input().split()))

new_arr = [-1]*n

for i in range(n):
  temp_value = 1001
  temp = -1
  for j in range(n):
    if temp_value > arr[j]:
      temp = j
      temp_value = arr[j]
      
  new_arr[temp] = i
  arr[temp] = 1001

for i in range(n):
  print(new_arr[i], end=' ')

      