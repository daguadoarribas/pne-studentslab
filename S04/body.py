from pathlib import Path
FILENAME = "sequences/U5.txt"

first_line = Path(FILENAME).read_text().find("\n")
body = Path(FILENAME).read_text()[first_line:]

print(body)

