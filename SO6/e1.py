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

    def __str__(self):
        return self.strbases
# Create objects of the class Seq
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")


