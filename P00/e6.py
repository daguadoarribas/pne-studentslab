from S06.Seq0 import *
seq_U5 = seq_read_fasta("../Sequences/U5.txt")
fragment = seq_U5[:20]
print("------| Exercise 6 |------")
print("Gene U5")
print("Fragment:", fragment)
print("Reverse:", seq_reverse(seq_U5, 20))
