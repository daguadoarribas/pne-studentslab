from Seq0 import *
print("-----| Exercise 3 |------")
filename = "U5.txt"
seq = seq_read_fasta(filename)
print(f"Gene U5 -> Length:", len(seq))

filename = "ADA.txt"
seq = seq_read_fasta(filename)
print(f"Gene ADA -> Length:", len(seq))

filename = "FRAT1.txt"
seq = seq_read_fasta(filename)
print(f"Gene FRAT1 -> Length:", len(seq))

filename = "FXN.txt"
seq = seq_read_fasta(filename)
print(f"Gene FXN -> Length:", len(seq))

