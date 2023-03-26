from collections import deque
n, k = map(int,input().split())

queue = deque([range(1, n+1)])

list = []

while len(queue) > 0:
    for i in range(k):
        if i == k-1:
            list.append(queue.popleft())
        else:
            queue.append(queue.popleft())

#출력부분
for i in range(n):
    if i ==0:
        print('<%d, '%list[i] ,end='')
    elif i == n-1:
        print('%d>'%list[i] ,end='')
    else:
        print('%d, '%list[i], end='')