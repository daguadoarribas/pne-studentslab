from Seq0 import *

print("-----| Exercise 6 |------")
seqU5 = seq_read_fasta("U5.txt")
fragment = seqU5[0:20]
print("Gene U5")
print("Fragment:", fragment)
print("Reverse:", seq_reverse(seqU5, 20))