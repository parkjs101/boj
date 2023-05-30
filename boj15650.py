n, m = map(int, input().split())

arr = [0]*10
isused = [False]*10

def func1(k, j):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    
    else:
        for i in range(j, n+1):
            if isused[i] == False:
                arr[k] = i
                isused[i] = True
                func1(k+1, i)
                isused[i] = False

func1(0, 1)
