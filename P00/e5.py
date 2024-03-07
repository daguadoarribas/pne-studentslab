from S06.Seq0 import *

seq_U5 = seq_read_fasta("../Sequences/U5.txt")
seq_ADA = seq_read_fasta("../Sequences/ADA.txt")
seq_FRAT1 = seq_read_fasta("../Sequences/FRAT1.txt")
seq_FXN = seq_read_fasta("../Sequences/FXN.txt")
print("------| Exercise 5 |------")
print("Gene U5:", seq_count(seq_U5), "\nGene ADA:", seq_count(seq_ADA), "\nGene FRAT1:", seq_count(seq_FRAT1), "\nGene FXN:", seq_count(seq_FXN))


