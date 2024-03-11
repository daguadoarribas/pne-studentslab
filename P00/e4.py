from S06.Seq0 import *

genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]
print("------| Exercise 4 |------")
for gene in genes:          ##itera sobre cada gen en la lista "genes"
    seq = seq_read_fasta(f"{gene}.txt")
    print(f"Gene: {gene}")

    for base in bases:          ##itera sobre cada base de la lista "bases"
        print(f"    Base {base}: {seq_count_base(seq, base)}")
