array = input()

def func1():
    if len(array) == 1:
        return print(0)
    stack = []
    numstack = []
    for i in range(len(array)):
        stack.append(array[i])
        if array[i] == '(':
            numstack.append(2)
            if array[i-1] == '(':
                
        elif array[i] == '[':
            numstack.append(3)
        