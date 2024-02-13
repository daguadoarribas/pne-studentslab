from SO6.Seq0 import *
FOLDER = "../Sequences/"
FILENAME = "U5.txt"

sequence = seq_read_fasta(FOLDER + FILENAME)
print(sequence[0:20])



