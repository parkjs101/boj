n = int(input())
nlist = list(map(int,input().split()))
ncount = 0
for i in range(n):
    cnt = 0
    for j in range(1,nlist[i]):
        if nlist[i]%j == 0:
            cnt += 1
    if cnt == 1:
        ncount += 1

print(ncount)
