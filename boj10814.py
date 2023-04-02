import sys
n = int(input())

li = []

for i in range(n):
    li.append(list(map(str, sys.stdin.readline().split())))

li.sort(key= lambda x: (int(x[0])))

for i in range(n):
    print(li[i][0], li[i][1])