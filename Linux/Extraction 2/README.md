# Extraction 2
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Identify the line that doesn't match the pattern of an MD5 hash.
```

<br>

## Requirements
- Regex
- Hash formats

<br>

## Solve
Use  `grep`:
```bash
grep -vE '^[a-fA-F0-9]{32}$' file.txt
```

You can also use my script: [solve.py](./solve/solve.py)

<br>

> Flag: `CSCTF{ce734e88ed1c2a3flagad39d7fec4fb3}`