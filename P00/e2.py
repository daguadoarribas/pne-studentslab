from S06.Seq0 import *
FOLDER = "../Sequences/"
FILENAME = "U5.txt"
print("------| Exercise 2 |------")
sequence = seq_read_fasta(FOLDER + FILENAME)
print(sequence[0:20])


