#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import socket
from generate_flag import generate_flag
import threading


questions = [
    {"question": "You have to make a script to connect to a server and send data. What programming language should you use?", "expected_answer": "python"},
    {"question": "Python, yeah! Now, what library is useful and widespread that you could take advantage of?", "expected_answer": "pwntools"},
    {"question": "Pwntool, exactly! Send me the function name to create a remote connection to a host.", "expected_answer": "remote"},
    {"question": "Easy, right? Send me the name of the function you use to receive a line of output.", "expected_answer": "recvline"},
    {"question": "Just a few more! What function is used to receive data from a remote process until a specific string is encountered?", "expected_answer": "recvuntil"},
    {"question": "You could do this all day! What do I use if I want to make sure I read all data from the socket until the connection is closed?", "expected_answer": "recvall"},
    {"question": "Good! What variable is used to set the log level in pwntools?", "expected_answer": "context.log_level"},
    {"question": "You are close... sort of. Send me the name of the function you use to send a line of input.", "expected_answer": "sendline"},
]

def handle_client(client_socket, addr):
    salt = "Pwntools"
    flag = generate_flag(salt)
    
    for i, question in enumerate(questions):
        client_socket.send((f"Question {i+1}\n" + question["question"]+"\n>> ").encode())
        client_socket.settimeout((len(questions)-i)/2+0.5)
        try:
            response = client_socket.recv(1024).decode().strip()
            if response.lower() != question["expected_answer"].lower():
                client_socket.send(b"Not quite, try again!\n")
                client_socket.close()
                return
        except socket.timeout:
            client_socket.send(b"\nToo slow, kiddo!\n")
            client_socket.close()
            return

    client_socket.send(f"\nCongratulations! Here's your flag: {flag}".encode() + b"\n")
    client_socket.close()

host = "0.0.0.0"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"Listening on {host}:{port}")

while True:
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()
