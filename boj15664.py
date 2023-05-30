n, m = map(int, input().split())

arr = [0]*10
isused = [False]*10
li = list(map(int, input().split()))
li.sort()
completed = set()

def func1(k, v):
    if k == m:
        v = []
        for i in range(m):
            v.append(str(arr[i]))
        a = " ".join(v)

        if a in completed:
            return
        
        print(a)
        completed.add(a)
        return
    
    for i in range(v, len(li)):
        if isused[i] != True:
            arr[k] = li[i]
            isused[i] = True
            func1(k+1, i)
            isused[i] = False

func1(0, 0)