from seq0 import *
print("-----| Exercise 2 |------")
filename = "U5.txt"
sequence = seq_read_fasta(filename)
print("The first 20 bases are:\n", sequence[:20])