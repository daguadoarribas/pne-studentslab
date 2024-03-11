from Seq0 import *

print("-----| Exercise 7 |------")
seqU5 = seq_read_fasta("U5.txt")
fragment = seqU5[0:20]
print("Gene U5")
print("Fragment:", fragment)
print("Complement:", seq_complement(seqU5, 20))