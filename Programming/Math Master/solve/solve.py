#!/usr/bin/python3

from pwn import *
from functools import reduce
import sys
import re

# python3 solve.py chal.chronossec.site 30080

context.log_level = "WARN"
# 'CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'NOTSET', 'WARN', 'WARNING'

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
s = remote(host, port)

def get_operation_and_numbers(text):
    parts = text.split(",")
    operation = parts[-1].split("\n")[0]
    numbers = parts[:-1]
    return operation, numbers

def read_server_message(s):
    message = s.recv().decode()
    print("Server says:", message)
    return message

while True:
    try:
        text = read_server_message(s)
        if "CSCTF" in text or not text:
            pattern = r"CSCTF{[0-9a-f]+}"
            flag = re.search(pattern, text).group(0)
            break

        operation, numbers_str = get_operation_and_numbers(text)
        numbers = [int(number) for number in numbers_str]

        if operation in ["add", "multiply", "subtract"]:
            if operation == "add":
                result = sum(numbers)
            elif operation == "multiply":
                result = reduce(lambda x, y: x * y, numbers)
            elif operation == "subtract":
                result = reduce(lambda x, y: x - y, numbers)
            
            print(f"Result: {result}")
            s.sendline(str(result).encode())
        else:
            print("Unknown operation or error message received")
            break
    except KeyboardInterrupt:
        exit("\nExiting...")

print("\n\Flag:", flag)
