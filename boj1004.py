T = int(input())
result = []
for i in range(T):
    count = 0
   
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())
    cx = [0]*n; cy = [0]*n; r = [0]*n

    for j in range(n):
        cx[j], cy[j], r[j] = map(int, input().split())

        d1 = (x1-cx[j])**2 + (y1-cy[j])**2
        d2 = (x2-cx[j])**2 + (y2-cy[j])**2
        radius = r[j]**2
        if radius > d1 and radius > d2:
            pass
        elif radius < d1 and radius < d2:
            pass
        else:
            count += 1

    result.append(count)

for i in range(len(result)):
    print(result[i])