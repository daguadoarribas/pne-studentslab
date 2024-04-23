from Seq1 import *
print("-----| Practice 1, Exercise 8 |------")
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print("  Bases:", s1.seq_count())
print("  Rev:", s1.reverse())
print("  Comp:", s1.complement())

print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print("  Bases:", s2.seq_count())
print("  Rev:", s2.reverse())
print("  Comp:", s2.complement())

print(f"Sequence 3: (Length: {s3.len()}) {s3}")
print("  Bases:", s3.seq_count())
print("  Rev:", s3.reverse())
print("  Comp:", s3.complement())