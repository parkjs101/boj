N, M = map(int, input().split())
s = []
check = []
count = 0
for i in range(N):
    s.append(input())
s = set(s)
for i in range(M):
    check.append(input())
    if check[i] in s:
        count += 1
print(count)
