n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

def fill(n, k, thing, d):
    for i in range(1, n+1):
        for j in range(1, k+1):
            w = thing[i][0] #무게 저장
            v = thing[i][1] #가치 저장

            if j < w:
                d[i][j] = d[i-1][j] #무게 초과로 i번째 물건을 못넣는 경우
            else:
                d[i][j] = max(d[i-1][j-w] + v, d[i-1][j]) #i번째 물건을 넣을 수 있는 경우

    return d[n][k]

result = fill(n, k, thing, d)
print(result)
