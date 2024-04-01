#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import socket
import threading
import random
import countryinfo
from generate_flag import generate_flag


CORRECT_ANSWERS_THRESHOLD = 30  

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
        self.countries = self.__get_all_capitals()
        self.banner = self.get_banner_from_file("banner.txt")

    def __get_all_capitals(self):
        try:
            countries = countryinfo.CountryInfo().all()

            capitals = {}
            for key in countries.keys():
                if "capital" in countries[key] and countries[key]["capital"] != '':
                    capitals[key] = countries[key]["capital"]

            return capitals
        except Exception as e:
            print(f"Error getting capitals: {e}")
            return {}

    def get_banner_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading banner file: {e}")
            return ''

    def start(self) -> None:
        try:
            self.server_socket.listen(5)
            while True:
                conn, address = self.server_socket.accept()
                threading.Thread(target=self.listen_to_client, args=(conn, address)).start()
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt received. Shutting down the server gracefully.")
        except Exception as e:
            print(f"An error occurred in start(): {e}")
        finally:
            self.server_socket.close()

    def listen_to_client(self, conn, address):
        salt = "Geography Master"
        flag = generate_flag(salt)
        try:
            conn.send(self.banner.encode())
            conn.send(b"\n[*] Welcome to Capitals master game!\n\n")
            conn.send(b"[+] To start the game press [1]\n")
            conn.send(b"[+] To view rules press [2]\n")

            choice = conn.recv(1024).decode().strip()

            if choice == '1':
                conn.send(b"\nLet the game begin!\n")
                countries_list = list(self.countries.keys())
                random.shuffle(countries_list)
                correct_answers_count = 0

                for country_name in countries_list[:CORRECT_ANSWERS_THRESHOLD]:  # Limit the number of questions
                    question = f"What is the capital of \"{country_name.title()}\"?\n"
                    conn.send(question.encode())
                    
                    try:
                        conn.settimeout(self.timeout)
                        answer = conn.recv(1024).decode().strip()

                        if answer.lower() == self.countries[country_name].lower():
                            correct_answers_count += 1
                            feedback = "Correct!\n"
                        else:
                            feedback = "Incorrect. Try again!\n"
                        
                        conn.send(feedback.encode())

                    except socket.timeout:
                        conn.send(b"Too slow mate. Bye bye\n")
                        break

                if correct_answers_count >= CORRECT_ANSWERS_THRESHOLD:
                    conn.send(flag.encode() + b"\n")
                else:
                    conn.send(b"Not enough correct answers. Bye bye\n")

            elif choice == '2':
                conn.send(b"\n[?] Answer correctly to all questions and you will receive a prize!\n[!] Good Luck!\n")

            conn.close()


        except ConnectionResetError:
            print("Connection reset by peer")
        except ValueError:
            conn.send(b"Invalid input. Please enter a valid integer.\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()


if __name__ == "__main__":
    server = Server(9999, "0.0.0.0")
    server.start()
