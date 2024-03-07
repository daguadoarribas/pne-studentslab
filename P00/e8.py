from S06.Seq0 import *

seq_U5 = seq_read_fasta("../Sequences/U5.txt")
seq_ADA = seq_read_fasta("../Sequences/ADA.txt")
seq_FRAT1 = seq_read_fasta("../Sequences/FRAT1.txt")
seq_FXN = seq_read_fasta("../Sequences/FXN.txt")

print("------| Exercise 8 |------")
print("Gene U5:", most_frequent_base(seq_U5))
print("Gene ADA:", most_frequent_base(seq_ADA))
print("Gene FRAT1:", most_frequent_base(seq_FRAT1))
print("Gene FXN:", most_frequent_base(seq_FXN))