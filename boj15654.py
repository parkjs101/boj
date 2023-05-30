n, m = map(int, input().split())

arr = [0]*10
isused = []

li = list(map(int, input().split()))
li.sort()

def func1(k):
    if k == m:
        for i in range(m):
            print(arr[i],end=' ')
        print()
        return
    
    for i in range(len(li)):
        if li[i] not in isused:
            arr[k] = li[i]
            isused.append(li[i])
            func1(k+1)
            isused.pop()

func1(0)