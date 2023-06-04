n = int(input())

arr = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    arr[i] = list(map(int, input().split()))

arr[0] = [0, 0]
if arr[1][0] == 1:
    dp[1] = arr[1][1]

for i in range(2, n+1):
    for j in range(1,i+1):
        if arr[i-j+1][0] == j:
            dp[i] = max(dp[i-j] + arr[i-j+1][1], dp[i])
        else:
            dp[i] = max(dp[i-j], dp[i])

print(dp[n])