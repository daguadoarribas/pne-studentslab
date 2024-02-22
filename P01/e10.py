from Seq1 import *

SEQUENCES = "../Sequences/"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Practice 1, Exercise 10 |-----")
for g in GENES:
    file = SEQUENCES + g + ".txt"
    s = Seq()
    s.read_fasta(file)
    dic = s.seq_count()
    ##print(dic) aquí printeo los diccionarios de cada file con la base y el num de veces que aparece
    maximum_base = max(dic, key = dic.get) ###Me mira el diccionario y coge la key que más se repite

    print("Gene " + g + ": Most frequent base: " + str(maximum_base))
