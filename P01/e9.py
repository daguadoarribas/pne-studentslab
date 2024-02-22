from Seq1 import *
# -- Create a Null sequence
s = Seq()
length = s.len()
FILENAME = "../Sequences/U5.txt"
# -- Initialize the null seq with the given file in fasta format
U5 = s.read_fasta(FILENAME)


print("Sequence: " + "(Length: " + str(length) + ")", U5, "\n" + "Bases: ", s.seq_count(), "\n" + "Rev: " + str(s.seq_reverse()), "\n" + "Comp: " + str(s.seq_complement()))
