n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

s = set()
arr = []

def func1(k, v):
    if k == m:
        if ' '.join(arr) not in s:
            print(' '.join(arr))
            s.add(' '.join(arr))
        return
    
    for i in range(v, n):
        arr.append(str(li[i]))
        func1(k+1, i)
        arr.pop()

func1(0, 0)

