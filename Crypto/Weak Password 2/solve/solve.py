import hashlib
import sys

with open("/usr/share/wordlists/rockyou.txt", "r", encoding='latin-1') as rockyou:
    passwords = rockyou.readlines()

for y in range(1985, 2000):
    for p in passwords:
        word = f"{p.strip()}_{y}"
        if hashlib.md5(word.encode()).hexdigest() == "077987b2cfc07b9a84a0007f288e9ed7":
            print(f"Password found: {word}")
            sys.exit()