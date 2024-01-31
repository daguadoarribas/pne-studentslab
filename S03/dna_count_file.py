with open("dna", "r") as f:
    dna_seq = {"A": 0, "C": 0, "T": 0, "G": 0}
    for line in f:
        for base in line:
            if base in dna_seq:
                dna_seq[base] += 1

        print(dna_seq)
