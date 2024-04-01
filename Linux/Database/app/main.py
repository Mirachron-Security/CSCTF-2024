#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import argparse
import random
import string
from faker import Faker
import hashlib
import mysql.connector
import docker
from datetime import datetime, timedelta
import time
from generate_flag import generate_flag
import logging

# Set up logging to file
logging.basicConfig(filename='output.log', filemode='a', format='%(asctime)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


salt = "Database"
num_users = 500

# ANSI escape codes for colored output
R = '\033[0;31m'  # Red
G = '\033[0;32m'  # Green
NC = '\033[0m'    # No Color


def gen_secret():
	characters = string.ascii_letters + string.digits
	secret = ''.join(random.choice(characters) for _ in range(74))
	return secret

def connect_and_update_database(user_data_list, secrets, connection_type, db_host, db_port):
	db_config = {
		'database': 'user_data',
		'user': 'root',
		'password': 'astrongrootpassword'
	}

	if connection_type == "local":
		db_config['host'] = 'localhost'
		db_config['port'] = db_port
	elif connection_type == "remote":
		db_config['host'] = db_host
		db_config['port'] = db_port
	elif connection_type == "docker":
		db_config['host'] = db_host  # Use the provided host (container IP)
		db_config['port'] = db_port

	try:
		conn = mysql.connector.connect(**db_config)
		cursor = conn.cursor()

		cursor.execute("CREATE DATABASE IF NOT EXISTS user_data;")
		cursor.execute("USE user_data;")

		cursor.execute("DROP TABLE IF EXISTS users;")

		cursor.execute('''
			CREATE TABLE IF NOT EXISTS users (
				id INT AUTO_INCREMENT PRIMARY KEY,
				username VARCHAR(255),
				real_name VARCHAR(255),
				email VARCHAR(255),
				phone_number VARCHAR(255),
				address VARCHAR(255),
				country VARCHAR(255),
				hashed_password VARCHAR(255),
				secret VARCHAR(255)
			)
		''')

		for user_data, secret in zip(user_data_list, secrets):
			cursor.execute('''
				INSERT INTO users (username, real_name, email, phone_number, address, country, hashed_password, secret)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
			''', (
				user_data["Usernames"][0],
				user_data["Real Names"][0],
				user_data["Email Addresses"][0],
				user_data["Phone Numbers"][0],
				user_data["Addresses"][0],
				user_data["Countries"][0],
				user_data["Hashed Passwords"][0],
				secret
			))

		random_user_index = random.randint(len(user_data_list)*4//7, len(user_data_list)*6//7)
		try:
			flag = generate_flag(salt) 
			cursor.execute('''
				UPDATE users
				SET secret = %s
				WHERE id = %s
			''', (flag, random_user_index + 1))

			conn.commit()
			message = f"Flag added: {flag}"
			print(f"{G}{message}{NC}")
			logging.info(f"[+] {message}")
		except:
			message = f"No eligible user found to assign the flag."
			print(f"{R}{message}{NC}")
			logging.info(f"[-] {message}")

	except mysql.connector.Error as err:
		if err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
			message = f"Error: Cannot connect to the MySQL server on {db_config['host']}:{db_config['port']}.\n"
			f"Please ensure the MySQL server is running and accepting connections."
			print(f"{R}{message}{NC}")
			logging.info(f"[-] {message}")
			# exit(1) # keep the container running
		else:
			message = f"MySQL Error: {err}"
			print(f"{R}{message}{NC}")
			logging.info(f"[-] {message}")
	finally:
		if 'conn' in locals():
			conn.close()


def get_container_ip(container_name):
	client = docker.from_env()
	try:
		container = client.containers.get(container_name)
		return container.attrs['NetworkSettings']['IPAddress']
	except docker.errors.NotFound:
		message = f"Error: Container '{container_name}' not found."
		print(f"{R}{message}{NC}")
		logging.info(f"[-] {message}")
		exit(1)

def calculate_next_interval():
    now = datetime.now()
    next_interval = (now + timedelta(minutes=5)).replace(second=0, microsecond=0)
    return (next_interval - now).total_seconds()

def main():
	while True:
		sleep_time = calculate_next_interval()
		message = f"Sleeping for {round(sleep_time)} seconds until the next interval.\n"
		print(message)
		logging.info(message)
		time.sleep(sleep_time)

		flag = generate_flag(salt)
		message = f"Generated flag: {flag}"
		print(message)
		# logging.info(message)

		connect_and_update_database(user_data_list, secrets, connection_type, db_host, db_port)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Database Update Script")
	parser.add_argument("-l", "--local", action="store_true", help="Connect locally to the database")
	parser.add_argument("-r", "--remote", metavar="REMOTE_IP", help="Connect remotely to the database")
	parser.add_argument("-c", "--container", metavar="CONTAINER_NAME", help="Docker container name to connect to")
	parser.add_argument("-p", "--port", metavar="PORT", type=int, help="Specify the port (optional)")

	args = parser.parse_args()

	# Determine the connection type based on the command-line arguments
	if args.local:
		connection_type = "local"
	elif args.remote:
		connection_type = "remote"
		remote_ip = args.remote
	elif args.container:
		connection_type = "docker"
		container_name = args.container
	else:
		message = f"Need help? Use -h (help)\n\n{R}Please specify either -l (local), -r (remote REMOTE_IP), or -c (container CONTAINER_NAME) option.{NC}"
		print(message)
		logging.info(message)
		exit(1)

	if args.port:
		port = args.port
	else:
		port = 3306  # Default MySQL port

	# If connecting to a Docker container, get its IP address
	if connection_type == "docker":
		container_ip = get_container_ip(container_name)
	else:
		container_ip = None

	fake = Faker()
	user_data_list = []

	for _ in range(num_users):
		user_data = {
			"Usernames": [fake.user_name()],
			"Real Names": [fake.name()],
			"Email Addresses": [fake.email()],
			"Phone Numbers": [fake.phone_number()],
			"Addresses": [fake.address()],
			"Countries": [fake.country()],
			"Hashed Passwords": [hashlib.sha256(fake.password().encode()).hexdigest()],
		}
		user_data_list.append(user_data)

	secrets = [gen_secret() for _ in user_data_list]

	# Connect to the database and update it
	if connection_type == "docker":
		db_host = container_ip
	elif connection_type == "local":
		db_host = "localhost"
	elif connection_type == "remote":
		db_host = remote_ip
	else:
		db_host = None  # Handle this case accordingly

	db_port = port

	connect_and_update_database(user_data_list, secrets, connection_type, db_host, db_port)
	main()
