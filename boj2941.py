word = input()
i = 0
num = 0
while(i<=len(word)-1):
    if word[i:i+2] == "c=" or word[i:i+2] == "c-" or word[i:i+2] == "d-" or word[i:i+2] == "lj" or word[i:i+2] == "nj" or word[i:i+2] == "s=" or word[i:i+2] == "z=":
        i += 2
        num += 1
    elif word[i:i+3] == "dz=":
        i += 3
        num += 1
    else:
        i += 1
        num += 1

print(num)


