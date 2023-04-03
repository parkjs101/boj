def n_six(n):
    s = str(n)
    if '666' in s:
        return True
    else:
        return False

num = int(input())
def find_num(num):
    count = 0
    n = 666
    while True:
        if num == count:
            break
        if n_six(n):
            count += 1
        n += 1
    return print(n-1)

find_num(num)