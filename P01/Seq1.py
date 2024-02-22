##Clase: tipo (animal, algo general)
##Objeto: un ejemplo especifico de una clase [variable + clase(...)]
#Clase: maquina > objeto:ordenador
#Característica: las funciones que yo tengo que llamar
#Las funciones de siempre son las caracteristicas y hay que llamarlas, las otras se asignan automaticamente al objeto
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases=None):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == None:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
            for i in strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    valid = True
                else:
                    valid = False
                    break
            if valid == True:
                print("New sequence created!")
                self.strbases = strbases
            else:
                print("INVALID sequence!")
                self.strbases = "ERROR"

    def len(self):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            length = 0
        else:
            length = len(self.strbases)
        return length

    def __str__(self):
        return self.strbases

    def seq_count_base(self, base):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            seq = ""
        else:
            seq = self.strbases

        sol = 0

        for i in seq:
            if i == base:
                sol += 1

        return sol

    def seq_count(self):
        dic = {"A": 0, "C": 0, "T": 0, "G": 0}
        if self.strbases == "ERROR" or self.strbases == "NULL":
            seq = ""
        else:
            seq = self.strbases

        for i in seq:
            if i in dic:
                dic[i] += 1
        return dic

    def seq_reverse(self):
        if self.strbases == "ERROR":
            reverse = "ERROR"
        elif self.strbases == "NULL":
            reverse = "NULL"
        else:
            sequence = self.strbases
            reverse = sequence[::-1]
        return reverse

    def seq_complement(self):
        if self.strbases == "ERROR":
            complement = "ERROR"
        elif self.strbases == "NULL":
            complement = "NULL"
        else:
            seq = self.strbases
            complement = ""
            for i in seq:
                if i == "A":
                    complement += "T"
                elif i == "T":
                    complement += "A"
                elif i == "C":
                    complement += "G"
                elif i == "G":
                    complement += "C"
        return complement

def read_fasta(self, filename):
    file_contents = Path(filename).read_text()
    first_line = file_contents.find("\n")
    new_sequence = file_contents[first_line:]
    self.strbases = new_sequence.replace("\n", "")
    return self.strbases
