n = int(input())
s = list(map(int, input().split()))

dp = [s[0]]

def lowerbound(li, v):
  left, right = 0, len(li)
  while left < right:
    mid = left + (right-left) // 2

    if li[mid] < v:
      left = mid+1
    else:
      right = mid
    
  return right

for i in range(1, n):
  if s[i] > dp[-1]:
    dp.append(s[i])
  else:
    k = lowerbound(dp, s[i])
    dp[k] = s[i]
    
print(len(dp))
