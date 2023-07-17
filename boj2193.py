n = int(input())
arr = [0]*100
arr[0] = 1
arr[1] = 1
arr[2] = 2
arr[3] = 3

for i in range(4, n):
  arr[i] = arr[i-1] + arr[i-2]

print(arr[n-1])