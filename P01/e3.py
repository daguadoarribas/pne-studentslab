from Seq1 import *

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence 1: ", str(s1) + "\n" + "Sequence 2: " + str(s2) + "\n" + "Sequence 3: " + str(s3))
