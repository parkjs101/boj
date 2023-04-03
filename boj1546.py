n = int(input())
score = list(map(int, input().split()))
score.sort()
max = score[n-1]
sum = 0
for i in range(n):
    sum += score[i]/max*100
print('%f'%(sum/n))
