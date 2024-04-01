#!/usr/bin/python3

import base64
import requests
import sys

def decode(string):
    # reverse
    string = string[::-1]
    print(string)

    # decode from base 64
    string = base64.b64decode(string.encode()).decode()
    print(string)

    # decode from hex
    string = bytes.fromhex(string).decode()
    print(string)

    # decode from decimal
    string = "".join(chr(int(string[i:i+2])) for i in range(0, len(string), 2))
    print(string)

    # decode from binary
    string = "".join(chr(int(string[i:i+8], 2)) for i in range(0, len(string), 8))
    return string

def main():
    if len(sys.argv) != 3:
        print("Usage: script.py <domain> <port>")
        sys.exit(1)

    domain = sys.argv[1]
    port = sys.argv[2]

    url = f"http://{domain}:{port}"
    r = requests.get(url=url)
    encoded_flag = r.text

    flag = decode(encoded_flag)
    print(flag)

if __name__ == "__main__":
    main()
