from Seq0 import *
print("-----| Exercise 4 |------")

genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for gene in genes:
    seq = seq_read_fasta(f"{gene}.txt")
    print(f"Gene {gene}:")

    for base in bases:
        print(f"    Base {base}: {seq_count_base(seq, base)}")