n, m = map(int, input().split())

arr = [0]*10

li = list(map(int, input().split()))
li.sort()

def func1(k, v):
    if k == m:
        for i in range(m):
            print(arr[i],end=' ')
        print()
        return
    
    for i in range(v, len(li)):
        arr[k] = li[i]
        func1(k+1, i)
            
func1(0, 0)