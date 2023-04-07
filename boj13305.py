import sys
n = int(input())

price_sum = 0
min_price = 1000000000

distance = list(map(int,sys.stdin.readline().split()))
point = list(map(int,sys.stdin.readline().split()))

for i in range(n-1):
    if min_price != 1000000000:
        min_price = min(min_price, point[i])
    else:
        min_price = point[i]
    
    price_sum += distance[i]*min_price

print(price_sum)
