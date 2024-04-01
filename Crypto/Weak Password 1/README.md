# Weak Password 1
Author: [Cujbă Mihai](https://www.linkedin.com/in/mihai-cujb%C4%83-109b8a72/)

<br>

## Description
```
Used a simple loop to find a hash match from a format combining 'football' and years.
```

<br>

## Requirements
- Hash cracking
- Automation

<br>

## Solve
To crack Jack's password:
1. Generate a wordlist from the years 1900 to 2020, appending "_football" to each year.
2. Calculate the MD5 hash of each word.
3. Compare each hash with the provided hash.

Here's a script to automate the process:

[Solve script](./solve/solve.py)

<br>

> Flag: `CSCTF{1993_football}`