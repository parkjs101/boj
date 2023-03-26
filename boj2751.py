import sys

N = int(sys.stdin.readline())
list = [0]*N

for i in range(N):
    list[i] = int(sys.stdin.readline())

list.sort()

for i in range(N):
    print(list[i])
