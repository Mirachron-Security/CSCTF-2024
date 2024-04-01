#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import yaml
import socket
import threading
import sys

BLACKLIST_PYTHON = ["os", "system", "pty"]
BLACKLIST_LINUX = ["cat", "tail", "head", "flag"]

class Client:

    username: str
    shopping_list: list

    def __init__(self, username) -> None:
        self.username = username
        self.shopping_list = list()

    def add_list(self, new_list) -> None:
        self.shopping_list.append(new_list)

    def store_list(self, data) -> bool:
        self.shopping_list.append(data)

class Server:

    max_size: int
    timeout: int
    host: str
    port: int
    server_socket: socket.socket
    countries: dict
    banner: str

    def __init__(self, port: int, host: str) -> None:
        self.host = host
        self.port = port
        self.timeout = 1
        self.max_size = 4096
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        

    def start(self) -> None:
        self.server_socket.listen(5)
        while True:
            conn, address = self.server_socket.accept()
            threading.Thread(target= self.listen_to_client, args=(conn, address)).start()
        
    def __get_options(self) -> bytes:
        return "\n[+] Welcome to our super secure shopping list application.\n[+] Press [1] to add a new list\n[+] Press [2] to see your lists\n".encode()

    def listen_to_client(self, conn, address):
        
        # Get username 
        conn.send(b"Enter your username: ")
        username = conn.recv(1024).decode()

        # Create client
        client = Client(username)
        conn.send(f"Hello, {username}".encode())
        
        while True:

            try:
                # Send payload
                conn.send(self.__get_options())
                try:
                    option = int(conn.recv(1024).decode())
                except ValueError:
                    conn.send(b"\nInvalid input: Please enter a valid integer.\n")
                    break

                if option == 1:
                    conn.send(b"\nEnter your list with the following format {[product name]: [quantity]}.\nExample: {apples: 10, bananas: 5}\n")
                    data = conn.recv(4096).decode()

                    if any(module in data for module in BLACKLIST_PYTHON):
                        conn.send(b"\nRCE detected!!!")
                        break

                    if any(command in data for command in BLACKLIST_LINUX):
                        conn.send(b"\nNaughty Naughty... Is not that easy!")
                        break

                    try:
                        result_list = yaml.load(data, Loader=yaml.Loader)
                        client.store_list(result_list)
                        
                    except Exception as err:
                        conn.send(b"\nInvalid format mate :(\n\n")
                        conn.send(str(sys.exc_info()).encode())
                        conn.send("\n")
                        

                elif option == 2:
                    conn.send(b"[*] Here are your lists:\n")
                    for index_list in range(len(client.shopping_list)):
                        conn.send(f"List {index_list}\n".encode())
                        conn.send(str(client.shopping_list[index_list]).encode())
                        conn.send(b"\n\n")
                else:
                    conn.send(b"\nInvalid option\n")
  
            except Exception as err:
                conn.send(str(sys.exc_info()).encode())
                break
        conn.close()
            
if __name__ == "__main__":
    server = Server(9999, "0.0.0.0")
    server.start()
