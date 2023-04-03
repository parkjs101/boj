N = int(input())

a = int(N/5)

def find_num(N):
    for i in range(a+1):
        if (N - (a-i)*5)%3 == 0:
            return (a-i + int((N - (a-i)*5)/3))
        else:
            continue
    return -1

print(find_num(N))
