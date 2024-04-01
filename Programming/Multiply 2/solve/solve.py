#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

from pwn import *
import re
import sys

# python3 solve.py chal.chronossec.site 30200

# context.log_level = "debug"

host = str(sys.argv[1])
port = int(sys.argv[2])
s = remote(host, port)

text = s.recv(1024).decode()
#print(text)
while 'Can you give me' in text:
    #print(text)
    match = re.search(r"me \[(.+?)\] exactly \[(\d+)\] times", text)
    #print(match)
    if match:
        number = match.group(1)
        char = int(match.group(2))
        response = char * number
        print('Response', response)
        s.sendline(response.encode())
    else:
        print(f"No match found for: {text}")

    text = s.recv(1024).decode()
    print(text)

s.close()