n, m = map(int, input().split())

arr = [0]*10

def func1(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    else:
        for i in range(1, n+1):
            arr[k] = i
            func1(k+1)

func1(0)