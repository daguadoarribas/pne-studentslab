from pathlib import Path

class Seq:

    def __init__(self, strbases=None):      ##strabases=None -> es un argumento opcional
        if strbases == None:
            print("NULL sequence created")      ##Esto es lo que se printea
            self.strbases = "NULL"
        else:
            for i in strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    valid = True
                else:
                    valid = False
                    break
            if valid == True:
                print("New sequence created")
                self.strbases = strbases
            else:
                print("Invalid sequence")
                self.strbases = "ERROR"

    def __str__(self):
        return self.strbases

    def read_fasta(self, filename):
        first_line = Path(filename).read_text().find("\n")
        sequence = Path(filename).read_text()[first_line:]
        self.strbases = sequence.replace("\n", "")
        return self.strbases

    def len(self):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            length = 0
        else:
            length = len(self.strbases)
        return length

    def seq_count_base(self, base):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            seq = ""
        else:
            seq = self.strbases
        count = 0
        for i in seq:
            if i == base:
                count += 1
        return count

    def seq_count(self):
        dict = {"A":0, "C":0, "G":0, "T":0}
        if self.strbases == "ERROR" or self.strbases == "NULL":
            seq = ""
        else:
            seq = self.strbases

        for i in seq:
            if i in dict:
                dict[i] += 1
        return dict

    def reverse(self):
        if self.strbases == "ERROR":
            reverse = "ERROR"
        elif self.strbases == "NULL":
            reverse = "NULL"
        else:
            reverse = self.strbases[::-1]
        return reverse


    def complement(self):
        if self.strbases == "ERROR":
            complement = "ERROR"
        elif self.strbases == "NULL":
            complement = "NULL"
        else:
            sequence = self.strbases
            complement = ""
            for i in sequence:
                if i == "A":
                    complement += "T"
                elif i == "C":
                    complement += "G"
                elif i == "G":
                    complement += "C"
                elif i == "T":
                    complement += "A"
        return complement

    def most_frequent_base(self):
        sequence = self.strbases
        base_counts = {base: sequence.count(base) for base in sequence}
        most_frequent_base = max(base_counts, key=base_counts.get)
        return most_frequent_base




