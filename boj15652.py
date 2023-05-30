n, m = map(int, input().split())

arr = [0]*10

def func1(k, v):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(v, n+1):
        arr[k] = i
        func1(k+1, i)

func1(0, 1)