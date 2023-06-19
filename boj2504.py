array = input()

def func1():
    if len(array) == 1:
        return print(0)
    stack = []
    numstack = []
    total = 0
    for i in range(len(array)):
        if array[i] == '(':
            stack.append(array[i])
            numstack.append(2)
        elif array[i] == '[':
            stack.append(array[i])
            numstack.append(3)
        elif array[i] == ')':
            if stack[-1] == '(':
                if len(stack)>2 and stack[-2] == '(':
                    numstack[-2] = numstack[-2]*numstack.pop()
                stack.pop()
                
            elif stack[-1]
            pass
        elif array[i] == ']':
            
            pass