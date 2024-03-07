from S06.Seq0 import *
seq_U5 = seq_read_fasta("../Sequences/U5.txt")
fragment = seq_U5[:20]
print("------| Exercise 7 |------")
print("Gene U5")
print("Fragment:", fragment)
print("Complement:", seq_complement(seq_U5, 20))