from collections import deque
N, M = map(int,  input().split()) 
li = list(map(int,input().split()))

q = deque(i+1 for i in range(N))
cnt = 0
for i in range(M):
    point = len(q)//2
    while q[0] != li[i]:
        if  point < q.index(li[i]):
            q.appendleft(q.pop())
            cnt += 1
        else:
            q.append(q.popleft())
            cnt += 1
    q.popleft()

print(cnt)

