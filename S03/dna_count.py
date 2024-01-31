input_sequence = input("Introduce the sequence: ")
print("Total length: ", len(input_sequence))
count = {"A": 0, "C": 0, "T": 0, "G": 0}

for i in input_sequence:
    if i == "A":
        count["A"] += 1
    elif i == "C":
        count["C"] += 1
    elif i == "T":
        count["T"] += 1
    elif i == "G":
        count["G"] += 1

for key, value in count.items():
    print(str(key) + ":", value)
