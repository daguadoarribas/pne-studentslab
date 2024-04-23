from seq0 import *

print("-----| Exercise 3 |------")
filename = "U5.txt"
seqU5 = seq_read_fasta(filename)
print("Gene U5 -> Length: ", seq_len(seqU5))

filename = "ADA.txt"
seqADA = seq_read_fasta(filename)
print("Gene ADA -> Length: ", seq_len(seqADA))

filename = "FRAT1.txt"
seqFRAT1 = seq_read_fasta(filename)
print("Gene FRAT1 -> Length: ", seq_len(seqFRAT1))

filename = "FXN.txt"
seqFXN = seq_read_fasta(filename)
print("Gene FXN -> Length: ", seq_len(seqFXN))