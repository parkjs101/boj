import sys

w = [[[0 for _ in range(21)]for _ in range(21)] for _ in range(21)]
w[0][0][0] = 1
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif w[a][b][c]:
        return w[a][b][c]
    
    else:
        for i in range(a):
            for j in range(b):
                for k in range(c):
                    
    

    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) +w(a-1, b, c-1) - w(a-1, b-1, c-1)


while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a+b+c == -3:
        break
    else:
        d = w(a, b, c)
        print('w(%d, %d, %d) = %d'%(a,b,c,d))

    