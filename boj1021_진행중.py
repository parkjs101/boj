from collections import deque
N, M = map(int,  input().split()) 
li = list(map(int,input().split()))

q = deque(i+1 for i in range(N))

for i in range(M):
    while True:
        if q[0]%len(q) == li[i]:
            q.popleft()
            break
        else:
            if len(q)//2 < li[i]- q[0]%len(q):
                q.append(q.popleft()+len(q))