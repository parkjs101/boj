grade = 0
credit = 0
for i in range(20):
    w = input().split(" ")
    s = float(w[1])
    if w[2] == "F":
        credit += s
    elif w[2] == "P":
        continue
    else:
        credit += s
        if w[2] == 'A+':
            grade += 4.5*s
        elif w[2] == 'A0':
            grade += 4*s
        elif w[2] == 'B+':
            grade += 3.5*s
        elif w[2] == 'B0':
            grade += 3*s
        elif w[2] == 'C+':
            grade += 2.5*s
        elif w[2] == 'C0':
            grade += 2*s
        elif w[2] == 'D+':
            grade += 1.5*s
        elif w[2] == 'D0':
            grade += 1*s            

print(grade/credit)