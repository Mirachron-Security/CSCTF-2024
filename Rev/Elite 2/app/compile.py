#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import os

SUCCESS = '\033[92m'
WARNING = '\033[93m'
END = '\033[0m'

current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "../files")
parent_dir = os.path.basename(os.path.abspath(os.path.join(current_dir, os.pardir)))

print(f"[+] '{parent_dir}'")
os.makedirs(output_dir, exist_ok=True)

def compile_and_print_status(source_file, output_file):
    source_file_name = os.path.basename(os.path.normpath(source_file))
    if os.path.exists(source_file):
        compile_command = f"gcc -fno-stack-protector -z execstack -no-pie -g -m32 '{source_file}' -o '{output_file}'"
        # print(f"[+] '{source_file_name}' was added.")
        return_code = os.system(compile_command)

        if return_code == 0:
            print(f"{SUCCESS}[+] Compilation successful: '{source_file_name}'{END}\n")
        else:
            print(f"{WARNING}[-] Compilation failed: '{source_file_name}'{END}\n")

# 'vuln' is for the user
# 'main' is for the server and contains the flag
compile_and_print_status(os.path.join(current_dir, "vuln.c"), os.path.join(output_dir, "vuln"))
compile_and_print_status(os.path.join(current_dir, "main.c"), os.path.join(current_dir, "main"))
