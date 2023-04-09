T = int(input())

cnt = [0]*1000000
cnt[0] = 1
cnt[1] = 2
cnt[2] = 4

for i in range(T):
    n = int(input())
    for i in range(2, n):
        cnt[i+1] = cnt[i] + cnt[i-1] + cnt[i-2]

    print(cnt[n-1])
    

