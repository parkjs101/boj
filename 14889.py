from collections import deque
n = int(input())

li = []
arr0 = [i for i in range(1, n+1)]
arr = [1]
isused = [False]*(n+1)
minimum = [100000000]

for i in range(n):
    li.append(list(map(int, input().split())))

def func1(k):
    global minimum
    if k == n//2:
        value = [0, 0]
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if i in arr and j in arr:
                    value[0] += li[i-1][j-1] + li[j-1][i-1]
                elif i not in arr and j not in arr:
                    value[1] += li[i-1][j-1] + li[j-1][i-1]
        if value[0] > value[1]:
            if minimum[0] > value[0]-value[1]:
                minimum.pop()
                minimum.append(value[0]-value[1])
        else:
            if minimum[0] > value[1]-value[0]:
                minimum.pop()
                minimum.append(value[1]-value[0])

    else:
        for i in range(2, n+1):
            if isused[i] != True and i > arr[-1]:
                arr.append(i)
                isused[i] = True
                func1(k+1)
                arr.pop()
                isused[i] = False

func1(1)
print(minimum)