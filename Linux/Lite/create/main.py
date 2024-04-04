#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import sqlite3
import os
import random
import string

def generate_random_string(length=27):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def create_random_entries(num_entries=100):
    # Set the output file path relative to the script
    output_directory = os.path.join(os.path.dirname(__file__), '..')
    output_file_path = os.path.join(output_directory, 'files', 'mydatabase.db')

    # Check if the '../files' directory exists, otherwise save to the current directory
    if not os.path.exists(os.path.join(output_directory, 'files')):
        output_file_path = 'mydatabase.db'

    connection = sqlite3.connect(output_file_path)
    cursor = connection.cursor()

    # Create 'users' table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')

    # Generate and insert random entries
    for i in range(1, num_entries + 1):
        username = generate_random_string()
        password = generate_random_string()

        # Add the flag entry at position 20
        if i == 20:
            username = "iIuseIaIflagIinIaIdatabaseI"
            password = "CSCTF{r3@d1ng_DAt@b2seS}"

        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

    connection.commit()
    connection.close()

def main():
    create_random_entries()

if __name__ == "__main__":
    main()
