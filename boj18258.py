from collections import deque
import sys
N = int(input())
queue = deque()

def push(x):
    return queue.append(x)

def pop():
    if len(queue) == 0:
        return print(-1)
    else:
        return print(queue.popleft())

def size():
    return print(len(queue))

def empty():
    if len(queue) == 0:
        return print(1)
    else:
        return print(0)
    
def front():
    if len(queue) == 0:
        return print(-1)
    else:
        return print(queue[0])

def back():
    if len(queue) == 0:
        return print(-1)
    else:
        return print(queue[-1])
    
for i in range(N):
    a = sys.stdin.readline().rstrip()

    if a[0:2] == 'pu':
        push(int(a[5:]))
    
    elif a[0] == 'p':
        pop()
    
    elif a[0] == 's':
        size()

    elif a[0] == 'e':
        empty()
    
    elif a[0] == 'f':
        front()

    elif a[0] == 'b':
        back()