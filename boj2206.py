import sys;sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
arr = []

for i in range(n):
  arr.append(*map(int, input()))

print(arr)