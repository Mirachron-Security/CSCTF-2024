#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import re, os

directory_loc = os.path.dirname(__file__)
file_path = os.path.join(directory_loc, "file.txt")

def nohex(line):
    pattern = re.compile(r'[^0-9A-Fa-f]')
    return bool(pattern.search(line))

# List to store lines with non-hexadecimal characters
lines = []

# Read the file line by line
with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()  # Remove leading/trailing whitespace and newline characters
        if nohex(line):
            lines.append((line_number, line))

# Print the lines with non-hexadecimal characters
for line_number, line in lines:
    print(f"Line {line_number}: CSCTF{{{line}}}")
