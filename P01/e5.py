from Seq1 import *
# -- Create a Null sequence
s1 = Seq()
length1 = s1.len()
# -- Create a valid sequence
s2 = Seq("ACTGA")
length2 = s2.len()
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")
length3 = s3.len()



print("Sequence 1: " + "(Length: " + str(length1) + ")", str(s1) + "\n" + "A:" + str(s1.seq_count_base("A")), "C:" + str(s1.seq_count_base("C")), "G:" + str(s1.seq_count_base("G")), "T:S" + str(s1.seq_count_base("T")))
print("Sequence 2: " + "(Length: " + str(length2) + ")", str(s2) + "\n" + "A:" + str(s2.seq_count_base("A")), "C:" + str(s2.seq_count_base("C")), "G:" + str(s2.seq_count_base("G")), "T:" + str(s2.seq_count_base("T")))
print("Sequence 3: " + "(Length: " + str(length3) + ")", str(s3) + "\n" + "A:" + str(s3.seq_count_base("A")), "C:" + str(s3.seq_count_base("C")), "G:" + str(s3.seq_count_base("G")), "T:" + str(s3.seq_count_base("T")))