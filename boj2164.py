from collections import deque
N = int(input())

c = deque(i+1 for i in range(N))

while len(c) != 1:
    c.popleft()
    c.append(c.popleft())

print(c[0])