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

def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        length = seq.len()
        sequence = seq
        print("Sequence" + str(index) + ": (Length:" + str(length) + ")", sequence)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)