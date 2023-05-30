n, m = map(int, input().split())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

cctv = [-1]*8
blind_spot_count = 64
cur = 0
rptcount = [4,2,4,4,1]
total_rptcount = 1

for i in range(n):
    for j in range(m):
        if li[i][j] != 0 or li[i][j] != 6:
            cctv[cur]= [[i,j], li[i][j], 0, 0] #cctv좌표, 종류, 방향, 반복카운트
            cur += 1

board = li #new board

def count():  #사각지대개수카운트함수
    return 0

blind_spot_count = min(count(), blind_spot_count)


                                

                


