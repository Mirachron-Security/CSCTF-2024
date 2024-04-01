#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import re, os

directory_loc = os.path.dirname(__file__)
file_path = os.path.join(directory_loc, "file.txt")

with open(file_path,"r") as file:
    contents = file.readlines()

pattern = r'^[A-Z]{4}[a-z]{6}\d[A-Z]\d{2}[a-zA-Z]{6}'

for line in contents:
    line = line.strip()
    if not re.match(pattern, line):
        flag = line

print(f"The flag is CSCTF{{{flag}}}")