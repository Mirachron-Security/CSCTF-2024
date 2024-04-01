# John
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Unlock a zip archive by cracking its password using John the Ripper.
```

<br>

## Requirements
- `john`
- `rockyou.txt` wordlist

<br>

## Solve
Extract the hash from the zip file and run it through John the Ripper:

```bash
zip2john hidden.zip > hash
john hash --wordlist=/usr/share/wordlists/rockyou.txt
```

If the hash was previously cracked:
```bash
john hash --show
```

Create script: [create.sh](./create/create.sh)

<br>

> Flag: `CSCTF{how_did_you_do_that?}`