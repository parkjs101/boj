import sys
N = int(input())
cards = set(map(int,sys.stdin.readline().split()))
M = int(input())
mlist = list(map(int,sys.stdin.readline().split()))
for i in range(len(mlist)):
    if mlist[i] in cards:
        mlist[i] = 1
    else:
        mlist[i] = 0

for i in range(len(mlist)):
    print(mlist[i], end=' ')