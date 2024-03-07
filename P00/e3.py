from S06.Seq0 import seq_read_fasta
FOLDER = "../Sequences/"
print("------| Exercise 3 |------")
FILENAME = "U5.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)
print("Gene U5 ->", len(sequence))

FILENAME = "ADA.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)
print("Gene ADA ->", len(sequence))

FILENAME = "FRAT1.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)
print("Gene FRAT1 ->", len(sequence))

FILENAME = "FXN.txt"
sequence = seq_read_fasta(FOLDER + FILENAME)
print("Gene FXN ->", len(sequence))
