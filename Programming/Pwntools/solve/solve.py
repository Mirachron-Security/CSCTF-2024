#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

from pwn import *
import sys

# python3 solve.py chal.chronossec.site 30210

context.log_level = "critical"

host = str(sys.argv[1])
port = int(sys.argv[2])

r = remote(host,port)

print(r.recvuntil(b">>").decode())
response = r.sendline(b"python")

print(r.recvuntil(b">>").decode())
response = r.sendline(b"pwntools")

print(r.recvuntil(b">>").decode())
response = r.sendline(b"remote")

print(r.recvuntil(b">>").decode())
response = r.sendline(b"recvline")

print(r.recvuntil(b">>").decode())
response = r.sendline(b"recvuntil")

print(r.recvuntil(b">>").decode())
response = r.sendline(b"recvall")

print(r.recvuntil(b">>").decode())
response = r.sendline(b"context.log_level")

print(r.recvuntil(b">>").decode())
response = r.sendline(b"sendline")

print(r.recvuntil(b": ").decode())

flag = r.recvall().decode()
print(flag)