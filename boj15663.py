n, m = map(int, input().split())

arr = [0]*10
isused = [False]*10
completed = set()

li = list(map(int, input().split()))
li.sort()

def func1(k):
    if k == m:
        v = []
        for i in range(m):
            v.append(str(arr[i]))
        a = " ".join(v)

        if a in completed:
            return
        
        for i in range(m):
            print(arr[i],end=' ')
        print()
        completed.add(a)
        return
    
    for i in range(len(li)):
        if isused[i] != True:
            arr[k] = li[i]
            isused[i] = True
            func1(k+1)
            isused[i] = False

func1(0)