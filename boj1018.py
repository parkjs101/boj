n, m = map(int,input().split())

c1 = [[0 for _ in range(n)] for _ in range(m)]
c2 = [[0 for _ in range(n)] for _ in range(m)]
c = [[0 for _ in range(n)] for _ in range(m)]

n1 = 0
n2 = 0

count = []

for i in range(8):
    for j in range(8):
        if (i%2 == 1 and j%2==1) or (i%2 == 0 and j%2 == 0):
            c1[i][j] = 'W'
            c2[i][j] = 'B'
        else:
            c1[i][j] = 'B'
            c2[i][j] = 'W'

for i in range(m):
    a = str(input())
    for j in range(n):
        c[i][j] = a[j]

for a in range(m-7):
    for b in range(n-7):

        for i in range(8):
            for j in range(8):
                if c[i+a][j+b] != c1[i][j]:
                    n1 += 1
                elif c[i+a][j+b] != c2[i][j]:
                    n2 += 1
        count.append(min(n1,n2))

print(min(count))
