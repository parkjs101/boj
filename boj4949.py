import sys

def balance():
    while True:
        s = sys.stdin.readline()
        li = []
        if s == '.\n':
            return -1
        else:
            for i in range(len(s)):
                if s[i] == '(' or s[i] == ')' or  s[i] == '[' or s[i] == ']':
                    li.append(s[i])
                    if len(li) > 1:
                        if (li[-1] == ')' and li[-2] == '(' ) or (li[-1] == ']' and li[-2] == '['):
                            li.pop()
                            li.pop()
                else:
                    pass
        if len(li) == 0:
            print('yes')
        else:
            print('no')     
balance()