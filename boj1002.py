import math

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if d == 0: #좌표가 같은 경우
        if r1 == r2: 
            print(-1)
        else:
            print(0)
    elif d < max(r1,r2): #원 중심이 원 안에
        if d + min(r1,r2) < max(r1,r2):
            print(0)
        elif d + min(r1,r2) == max(r1,r2):
            print(1)
        else:
            print(2)
    elif d == max(r1,r2): #원 중심이 원에
        print(2)
    elif d > max(r1,r2): #원 중심이 원 밖에
        if d < r1 + r2:
            print(2)
        elif d == r1+r2:
            print(1)
        else:
            print(0)
    


