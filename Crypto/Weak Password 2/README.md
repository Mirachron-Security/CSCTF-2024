# Weak Password 2
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Brute-forced a hash by iterating through a wordlist appended with years.
```

<br>

## Requirements
- Hash cracking
- Automation

<br>

## Solve
Create a script to brute-force the target hash using a combination of `rockyou.txt` passwords and a range of years. 
Match each generated hash against the target to find the correct password:

[Solution script](./solve/solve.py)

<br>

> Flag: `CSCTF{dragon_1987}`
