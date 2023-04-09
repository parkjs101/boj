def climbing():
    n = int(input())
    stair = [0]*n

    for i in range(n):
        stair[i] = int(input())
    
    if n == 1:
        return print(stair[0])
    elif n == 2:
        return print(stair[0]+stair[1])
    else:
        score = [[0]for i in range(n)]
        score[0] = [stair[0]]
        score[1] = [score[0][0]+stair[1], stair[1]]

        for i in range(2, n):
            score[i] = [score[i-1][1]+stair[i], max(score[i-2])+stair[i]]

        return print(max(score[-1]))
climbing()