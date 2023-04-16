N = int(input())

n = [0]*1000005
n[1] = 1
n[2] = 2

for i in range(3, N+1):
    n[i] = (n[i-1] + n[i-2])%15746

print(n[N])