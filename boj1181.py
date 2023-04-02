import sys
n = int(input())
li = []

for i in range(n):
    li.append(sys.stdin.readline().strip())

li = list(set(li))
li.sort(key = lambda x: (len(x), x))

for i in range(len(li)):
    print(li[i])