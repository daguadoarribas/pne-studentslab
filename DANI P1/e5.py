from Seq1 import *
print("-----| Practice 1, Exercise 5 |------")
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print(f"A:"s1.seq_count_base())
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print(s2.seq_count_base())
print(f"Sequence 3: (Length: {s3.len()}) {s3}")
print(s2.seq_count_base())