from Seq1 import *
# -- Create a Null sequence
s = Seq()
filename = "../Sequences/U5.txt"
U5 = s.read_fasta(filename)

print("-----| Practice 1, Exercise 9 |------")
print("Sequence: (Length:", s.len(), ")", U5)
print("  Bases:", s.seq_count())
print("  Rev:", s.reverse())
print("  Comp:", s.complement())
