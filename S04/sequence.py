from pathlib import Path
FILENAME = "sequences/ADA.txt"

first_line = Path(FILENAME).read_text().find("\n")
body = Path(FILENAME).read_text()[first_line:]
body = body.replace("\n", "")

print(len(body))