import sys
n, m = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board.append(sys.stdin.readline().rstrip()) 

case = 999999999999

for i in range(n-7):
    for j in range(m-7):
        case1 = 0
        case2 = 0
        for l in range(8):
            for k in range(8):
                if (i+j+k+l)%2 == 0:
                    if board[i+k][j+l] == 'W':
                        case1 += 1
                    else:
                        case2 += 1
                else:
                    if board[i+k][j+l] == 'B':
                        case1 += 1
                    else:
                        case2 += 1

        case = min(case1, case2, case)

print(case)

