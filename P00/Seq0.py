from pathlib import Path
def seq_ping():
    print("OK")
def seq_read_fasta(filename):
    first_line = Path(filename).read_text().find("\n")
    body = Path(filename).read_text()[first_line:]
    body = body.replace("\n", "")
    return body

def seq_len(filename):
    first_line = Path(filename).read_text().find("\n")
    body = Path(filename).read_text()[first_line:]
    body = body.replace("\n", "")
    return len(body)

def seq_count_base(seq, base)