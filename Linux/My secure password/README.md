# My secure password
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Crack Linux user password hashes to find the longest password.
```

<br>

## Requirements
- Understanding Linux filesystem and password storage
- `unshadow` and `john`
- `rockyou.txt` wordlist

<br>

## Solve
Use `unshadow` to merge the `passwd` and `shadow` files, then crack with `john`.

```bash
unzip chall.zip
sudo unshadow passwd shadow > hash-all.txt
grep 'bash$' hash-all.txt | grep -v root > hash-users.txt
john --format=crypt hash-users.txt --wordlist=/usr/share/wordlists/rockyou.txt
john hash-users.txt --show
```

The longest password extracted will be `manchesterunited`.

<br>

>  Flag: `CSCTF{manchesterunited}`