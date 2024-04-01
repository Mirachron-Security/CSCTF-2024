# Decoding
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Decode a complex QR image that hides binary and base64 encoded data.
```

<br>

## Requirements
- QR decoding
- Binary code understanding
- Base64 decoding

<br>

## Solve
First, decode the QR code to binary data, then convert the binary code to a text string. 
Finally, decode the base64 encoded string 5 times to reveal the flag.

Refer to [solve.py](./solve/solve.py) to see how to get the flag.

If you're curious about the creation process, check out [create.py](./create/create.py).

<br>

> Flag: `CSCTF{@nOth3r_h1dd3N_f12g}`
