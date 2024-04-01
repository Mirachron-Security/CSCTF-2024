#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import socket
import random
import threading
import time

messages = [
	"Are you done yet?",
	"What are you trying to do?",
	"I think you should just quit.",
	"No comment.",
	"Try again or something",
	"Can you stop that?"
]

def handle_client(client_socket):
	client_socket.send(b"Math expression: ")
	expression = client_socket.recv(1024).decode().strip()

	if ("import" or "system") in expression:
		client_socket.send(b"Why do you want to hack?\n")
		client_socket.close()
		return
	if "flag" in expression:
		client_socket.send(b"Ooooh... you are looking for the flag?\n")
		time.sleep(3)
		client_socket.send(b"Keep looking!\n")
		client_socket.close()
		return


	try:
		result = str(eval(expression))
		client_socket.send(b"Answer: " + result.encode() + b"\n")
	except ZeroDivisionError:
		client_socket.send(b"Really? You think dividing by zero will do it?\n")
	except (NameError, SyntaxError):
		client_socket.send(random.choice(messages).encode() + b"\n")

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
	client_handler = threading.Thread(target=handle_client, args=(client_socket,))
	client_handler.start()
