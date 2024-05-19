def accepted_bases(strbases):
    valid = True
    for i in strbases:
        if i not in Seq.bases:
            valid = False
            break
    return valid


class Seq:

    bases = ["A", "C", "T", "G"]
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}

    def __init__(self, strbases=None):
        if strbases is None or len(strbases) == 0:
            self.strbases = "NULL"
            print("NULL sequence created")
        elif accepted_bases(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INVALID sequence!")


    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            length = 0
        else:
            length = len(self.strbases)
        return length

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            count = 0
        else:
            count = self.strbases.count(base)
        return count

    def count(self):
        dict_bases = {}
        for i in Seq.bases:
            dict_bases[i] = self.count_base(i)
        return dict_bases

    def reverse(self):
        if self.strbases == "NULL":
            reverse = "NULL"
        elif self.strbases == "ERROR":
            reverse = "ERROR"
        else:
            reverse = self.strbases[::-1]
        return reverse

    def complement(self):
        if self.strbases == "NULL":
            complement_seq = "NULL"
        elif self.strbases == "ERROR":
            complement_seq = "ERROR"
        else:
            complement_seq = ""
            for i in self.strbases:
                complement_seq += Seq.complements[i]
        return complement_seq

    def read_fasta(self, filename):
        from pathlib import Path
        file_content = Path(filename).read_text()
        lines = file_content.splitlines()
        body = lines[1:]
        self.strbases = ""
        for line in body:
            self.strbases += line

    def max_base(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return None
        max_base = ""
        max_count = 0
        for base in Seq.bases:
            count = self.count_base(base)
            if count > max_count:
                max_count = count
                max_base = base
        return max_base

    def info(self):
        i = f"Total length: {self.len()}\n"
        for base in Seq.bases:
            if self.len() == 0:
                percentage = 0
            else:
                percentage = round((self.count_base(base) * 100) / self.len(), 1)
            i += f"{base}: {self.count_base(base)} ({percentage}%)\n"
        return i
