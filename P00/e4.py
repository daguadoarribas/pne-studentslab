countA = 0
countC = 0
countT = 0
countG = 0

for i in FILENAME:
    if i == "A":
        countA += 1
    elif i == "C":
        countC += 1
    elif i == "G":
        countG += 1
    elif i == "T":
        countT += 1