n = int(input())
li = []
arr = []
value = [0,0]
m = n*(n-1)//2
isused = [0]*(n+1)
minimum = []

for i in range(n):
    li.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i >= j:
            continue
        arr.append([i, j])

print(arr)

def func1(k, x):
    if k == n//2:
        if value[0] > value[1]:
            minimum.append(value[0]-value[1])
        else:
            minimum.append(value[1]-value[0])
        return
    else:
        for i in range(n):
            for j in range(n):
                if i >= j or isused[i] != 0 or isused[j] != 0:
                    continue
                else:
                    isused[i] = 1
                    isused[j] = 1
                    value[x] += li[i][j] + li[j][i]
                    func1(k+1,1-x)
                    value[x] -= li[i][j] + li[j][i]
                    isused[i] = 0
                    isused[j] = 0
"""
            if isused[arr[i][0]] == 0 and isused[arr[i][1]] == 0:
                isused[arr[i][0]] = 1
                isused[arr[i][1]] = 1
                v = li[arr[i][0]-1][arr[i][1]-1] + li[arr[i][1]-1][arr[i][0]-1]
                value[x] += v
                func1(k+1,1-x)
                value[x] -= v
                isused[arr[i][0]] = 0
                isused[arr[i][1]] = 0 """

func1(0, 0)
print(min(minimum))
