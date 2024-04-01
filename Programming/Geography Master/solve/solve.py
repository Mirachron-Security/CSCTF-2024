#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

from pwn import *
from countryinfo import CountryInfo
import sys

# python3 solve.py chal.chronossec.site 30070

context.log_level = "WARN"
# 'CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'NOTSET', 'WARN', 'WARNING'

def get_capital(country_name):
    try:
        country = CountryInfo(country_name)
        capital = country.capital()
        return capital
    except Exception as e:
        print(f"Error fetching capital for {country_name}: {e}")
        return None

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <host> <port>")
        sys.exit(1)

    host, port = sys.argv[1], int(sys.argv[2])

    # Establish connection
    r = remote(host, port)

    # Read initial messages and prompts from the server
    r.recvuntil(b"To start the game press [1]\n")

    # Start the game
    r.sendline(b"1")

    while True:
        # Fetching the next question
        prompt = r.recvuntil(b'?\n').decode()
        print(f"Received prompt: {prompt}")

        # Extract the country name
        country = prompt.split('"')[1]
        print(f"Country: {country}")

        # Fetch the capital
        capital = get_capital(country)
        if capital:
            print(f"Answer: {capital}")
            r.sendline(capital.encode())
        else:
            print("No capital found, sending a blank response.")
            r.sendline(b'')

        # Attempt to read a response, looking for either another question or the flag
        try:
            response = r.recvuntil([b'What is the capital of', b'CSCTF{'], timeout=5)
            if b'CSCTF{' in response:
                print("[+] Flag found:", response.decode())
                break
        except EOFError:
            print("[-] Connection closed by the server.")
            break
        except Exception as e:
            print(f"[*] An unexpected error occurred: {e}")
            break

    # Close the connection
    r.close()

if __name__ == "__main__":
    main()
