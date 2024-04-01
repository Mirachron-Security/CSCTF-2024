# Multiply 2
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Continue from Multiply 1 and keep sending characters as requested by the server to get the flag.
```

<br>

## Requirements
- Connect to servers
- Automation
- Regex

<br>

## Solve
You need to keep interacting with the server, sending back characters according to the server's request until the flag is received.

View the [solve.py](./solve/solve.py) script.

Compared to `Multiply 1`, you have to send different data multiple times in a single connection.

<br>

> Flag: `CSCTF{hash-that-changes-every-5-minutes}`