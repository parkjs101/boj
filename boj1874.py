import sys
def stackcount():
    result = []
    n = int(input())
    li = [0]
    stack = []
    popped = set([])
    for i in range(n):
        li.append(int(sys.stdin.readline().strip()))

    for i in range(1, n+1):
        if li[i] > li[i-1]:
            for j in range(li[i-1]+1, li[i]+1):
                if j in popped:
                    continue
                else:
                    stack.append(j)
                    result.append('+')

            popped.add(stack.pop())
            result.append('-')

        elif li[i] < li[i-1]:
            if li[i] == stack[-1]:
                popped.add(stack.pop())
                result.append('-')
            else:
                return print('NO')
            
    for i in range(len(result)):
        print(result[i])
    return 0

stackcount()            





