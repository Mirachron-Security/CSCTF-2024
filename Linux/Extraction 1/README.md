# Extraction 1
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Isolate a unique line from the given text file using regular expressions.
```

<br>

## Requirements
- Regex
- `grep`

<br>

## Solve
Use `grep` to exclude lines that match the specific pattern:

```bash
grep -E -v '^[A-Z]{4}[a-z]{6}\d[A-Z]\d{2}[a-zA-Z]{6}$' file.txt
```

You can also use my script: [solve.py](./solve/solve.py)

<br>

> Flag: `CSCTF{FGMQzggbiy3E864BQbpr}`