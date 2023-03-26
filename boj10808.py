s = input()
a = [0]*26
for i in range(len(s)):
    n = int(ord(s[i])) - 97
    a[n] += 1

for i in range(26):
    print(a[i],end=" ")
