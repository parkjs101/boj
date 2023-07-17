n = int(input())
s = list(map(int,input().split()))

dp = [0]*(n)

for i in range(n):
    for j in range(i):
        if s[j] < s[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
    if dp[i] == 0:
        dp[i] = 1

dp.sort()
print(dp[n-1])