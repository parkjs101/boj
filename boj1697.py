from collections import deque
n, k = map(int, input().split())
arr = [-1]*100005
arr[n] = 0
q = deque()
q.append(n)

def func1():
    if n == k:
        return print(0)
    while q:
        cur = q[0]
        count = arr[cur]
        if q[0] == k:
            return print(count)
        q.popleft()
        if cur-1 >= 0 and arr[cur-1] == -1:
            q.append(cur-1)
            arr[cur-1] = count+1
        if cur+1 <= 100000 and arr[cur+1] == -1:
            q.append(cur+1)
            arr[cur+1] = count+1
        if cur*2 <= 100000 and arr[cur*2] == -1:
            q.append(cur*2)
            arr[cur*2] = count+1

func1()

