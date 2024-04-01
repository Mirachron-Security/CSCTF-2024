#!/usr/bin/python3

import socket
import signal
import sys
import threading
import random
from functools import reduce
from generate_flag import generate_flag

salt = "Math Master"

class Server:
    max_size = 4096
    timeout = 2

    def __init__(self, port: int, host: str) -> None:
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.keep_running = True  

    def signal_handler(self, sig, frame):
        print("\nShutting down the server gracefully.")
        self.keep_running = False
        self.server_socket.close()
        sys.exit(0)

    def start(self) -> None:
        signal.signal(signal.SIGINT, self.signal_handler)
        self.server_socket.listen(5)
        print("Server started. Waiting for connections...")
        while self.keep_running:
            try:
                conn, address = self.server_socket.accept()
                print(f"Connection established with {address}")
                conn.settimeout(self.timeout)
                threading.Thread(target=self.listen_to_client, args=(conn, address)).start()
            except KeyboardInterrupt:
                self.signal_handler(signal.SIGINT, None)

    def __generate_random_numbers(self):
        operations = ["add", "multiply", "subtract"]
        len_numbers = random.randint(5, 20)
        numbers = [str(random.randint(500, 1000)) for _ in range(len_numbers)]
        operation_index = random.randint(0, 2)
        numbers.append(operations[operation_index])
        return numbers

    def calculate_result(self, numbers: list) -> int:
        integer_list = [int(x) for x in numbers[:-1]]
        operation = numbers[-1]
        if operation == "add":
            return sum(integer_list)
        elif operation == "multiply":
            return reduce(lambda x, y: x * y, integer_list)
        elif operation == "subtract":
            return reduce(lambda x, y: x - y, integer_list)

    def send_message(self, conn, message):
        try:
            conn.send(message)
        except BrokenPipeError:
            print("Client disconnected.")
            return False
        return True

    def listen_to_client(self, conn, address):
        correct_result_count = 0
        while True:
            try:
                numbers = self.__generate_random_numbers()
                payload = (','.join(numbers) + "\nAnswer: ").encode()
                result = self.calculate_result(numbers)

                conn.settimeout(self.timeout)
                if not self.send_message(conn, payload):
                    break

                data = conn.recv(self.max_size).decode().strip()

                if not data:
                    break

                try:
                    client_answer = int(data)
                except ValueError:
                    if not self.send_message(conn, b"Invalid input: Please enter a valid integer.\n"):
                        break
                    continue

                if client_answer == result:
                    correct_result_count += 1
                else:
                    if not self.send_message(conn, b"Wrong :("):
                        break
                    continue

                if correct_result_count == 50:
                    flag = generate_flag(salt)
                    if not self.send_message(conn, flag.encode()):
                        break
            except socket.timeout:
                if not self.send_message(conn, b"\nToo slow mate. Bye!\n"):
                    break
            except ConnectionResetError:
                print("Connection reset by peer")
                break

        conn.close()

def main():
    server = Server(9999, "0.0.0.0")
    server.start()

if __name__ == "__main__":
    main()
