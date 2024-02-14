import termcolor
class Seq:
    def __init__(self, strbases):
        self.strbases = strbases            ###to define the object that is being called in the method -- para acceder a las caracteristicas de un objeto
        for i in strbases:
            if i == "A" or i == "C" or i == "G" or i == "T":
                solution = True
            else:
                solution = False
                break
        if solution:
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("ERROR!!")

    def len(self):
        return self.strbases

    def __str__(self):
        return self.strbases

def print_seqs(seq_list, color):
    for index, seq in enumerate(seq_list):
        length = seq.len()
        sequence = seq
        termcolor.cprint(("Sequence" + str(index) + ": (Length:" + str(length) + ") " + str(sequence)), color)

def generate_seqs(pattern, number):
    new_list = []
    for i in range(1, number + 1):
        new_list.append(Seq(pattern * i))
    return new_list

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")


termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")
