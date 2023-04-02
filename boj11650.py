import sys

N = int(input())

li = []
for i in range(N):
    li.append(list(map(int,sys.stdin.readline().split())))

li.sort(key=lambda x:(x[0], x[1]))

for i in range(len(li)):
    print(li[i][0], li[i][1])