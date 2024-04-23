from Seq0 import *

print("-----| Exercise 8 |------")
seqU5 = seq_read_fasta("U5.txt")
seqADA = seq_read_fasta("ADA.txt")
seqFRAT1 = seq_read_fasta("FRAT1.txt")
seqFXN = seq_read_fasta("FXN.txt")

print("Gene U5: Most frequent base:", most_frequent_base(seqU5))
print("Gene ADA: Most frequent base:", most_frequent_base(seqADA))
print("Gene FRAT1: Most frequent base:", most_frequent_base(seqFRAT1))
print("Gene FXN: Most frequent base:", most_frequent_base(seqFXN))