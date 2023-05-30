while True:
    N = str(input())
    if N == '0':
        break
    else:
        if len(N) == 1:
            print('yes')
            continue
        else:
            for i in range(len(N)//2):
                if N[i] == N[len(N)-i-1]:
                    flag = True
                else:
                    print('no')
                    flag = False
                    break
            if flag == True:
                print('yes')
