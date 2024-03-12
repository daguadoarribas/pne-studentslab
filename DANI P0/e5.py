from Seq0 import *

print("-----| Exercise 5 |------")
seqU5 = seq_read_fasta("U5.txt")
seqADA = seq_read_fasta("ADA.txt")
seqFRAT1 = seq_read_fasta("FRAT1.txt")
seqFXN = seq_read_fasta("FXN.txt")

print(f"Gene U5:", seq_count(seqU5))
print(f"Gene ADA:", seq_count(seqADA))
print(f"Gene FRAT1:", seq_count(seqFRAT1))
print(f"Gene FXN:", seq_count(seqFXN))