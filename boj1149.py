import sys
n= int(input())

cost = [[0] for i in range(n)]

for i in range(n):
    cost[i] = list(map(int, sys.stdin.readline().split()))

sum = [[0] for i in range(n)]

