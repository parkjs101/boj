import sys
T = int(input())
for i in range(T):
	M, N, K = map(int, input().split())
	xy = [[0]*M for _ in range(N)]
	li = []
	for i in range(K):
		x, y = map(int, sys.stdin.readline().split())
		li.append[x,y]
		xy[x][y] = 1

	visited = []
	w = K
	for i in range(K):
		for j in range(i+1, K):
			li[i]
	print(w)
