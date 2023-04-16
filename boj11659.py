import sys

N, M = map(int, input().split())

num = list(map(int,input().split()))
sum = [0]*N

for i in range(0, len(num)):
    if i == 0:
        sum[i] = num[0]
    else:
        sum[i] = sum[i-1] + num[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i != j:
        if i-1>0:
            print(sum[j-1]-sum[i-2])
        else:
            print(sum[j-1])
            
    else:
        print(num[i-1])

