from Seq0 import seq_read_fasta
FOLDER = "../Sequences/"
FILENAME = "U5.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)

countA = 0
countC = 0
countT = 0
countG = 0

for i in sequence:
    if i == "A":
        countA += 1
    elif i == "C":
        countC += 1
    elif i == "T":
        countT += 1
    elif i == "G":
        countG += 1
print("Gene U5: ", "A ->", countA, "C ->", countC, "T ->", countT, "G ->", countG)

FILENAME = "ADA.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)

countA = 0
countC = 0
countT = 0
countG = 0

for i in sequence:
    if i == "A":
        countA += 1
    elif i == "C":
        countC += 1
    elif i == "T":
        countT += 1
    elif i == "G":
        countG += 1
print("Gene ADA: ", "A ->", countA, "C ->", countC, "T ->", countT, "G ->", countG)

FILENAME = "FRAT1.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)

countA = 0
countC = 0
countT = 0
countG = 0

for i in sequence:
    if i == "A":
        countA += 1
    elif i == "C":
        countC += 1
    elif i == "T":
        countT += 1
    elif i == "G":
        countG += 1
print("Gene FRAT1: ", "A ->", countA, "C ->", countC, "T ->", countT, "G ->", countG)

FILENAME = "FXN.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)

countA = 0
countC = 0
countT = 0
countG = 0

for i in sequence:
    if i == "A":
        countA += 1
    elif i == "C":
        countC += 1
    elif i == "T":
        countT += 1
    elif i == "G":
        countG += 1
print("Gene FXN: ", "A ->", countA, "C ->", countC, "T ->", countT, "G ->", countG)