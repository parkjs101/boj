n, m = map(int, input().split())
arra = []
arrb = []
for i in range(n):
    arra.append(list(input()))
for i in range(n):
    arrb.append(list(input()))

def func1(arra, arrb):
    count = 0
    if n < 3 or m < 3:
        if arra == arrb: #바꿀수 없지만 같으면 0출력
            return print(count)
        else:
            return print(-1)
    
    else:
        for i in range(n-2):
            for j in range(m-2):

                if arra[i][j] != arrb[i][j]:
                    for k in range(3):
                        for l in range(3):
                            if arra[i+k][j+l] == '0':
                                arra[i+k][j+l] = '1'
                            else:
                                arra[i+k][j+l] = '0'
                    count += 1
                if arra == arrb:
                    return print(count)
        return print(-1)

func1(arra, arrb)