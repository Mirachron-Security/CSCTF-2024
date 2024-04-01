#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import socket
import threading
import string
import random
from generate_flag import generate_flag

salt = "Multiply 1"

host = "0.0.0.0"
port = 9999
print(f"Listening on {host}:{port}")

def get_prompt(choice):
    char = random.choice(choice)
    number = random.randint(200, 500)
    
    prompt = f"Can you give me [{char}] exactly [{number}] times?\n"
    answer = str(char) * number
    
    return prompt, answer

def handle_client(client_socket, addr):
    char = string.ascii_letters
    try:
        prompt, answer = get_prompt(char)
        client_socket.settimeout(3)
        client_socket.send(prompt.encode())

        try:
            response = client_socket.recv(1024).decode().strip()
            if response != answer:
                client_socket.send(b"You are awfully wrong!\nExpected:")
                client_socket.send(answer.encode())
                client_socket.close()
                return
        
        except socket.timeout:
            client_socket.send(b"\nYou need more speed!\n")
            client_socket.close()
            return

        flag = generate_flag(salt)
        client_socket.send(f"Congratulations! Here's your flag: {flag}".encode())
        client_socket.close()
    except OSError as e:
        print(f"OSError: {e}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen(1)

try:
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.close()
