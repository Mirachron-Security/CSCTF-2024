# 3.146416102
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
The challenge involves decoding a flag encoded through multiple layers.
The name "3.146416102" hints at the encoding bases used: 64 (Base64), 16 (hexadecimal), 10 (decimal), and 2 (binary).
```

<br>

## Requirements
- Decoding
- Automation

<br>

## Solve
The encoded flag goes through five steps: binary conversion, decimal transformation, hexadecimal encoding, Base64 encoding, and finally, reversal. 

To decode:

1. **Reverse** the encoded string to its pre-reversal state.
2. **Base64 Decode** to revert from Base64 encoding.
3. **Hexadecimal to Decimal Conversion** to decode from hexadecimal.
4. **Decimal to Binary Conversion** to reverse the decimal transformation.
5. **Binary to ASCII Conversion** to obtain the original flag characters.

The solution script automates the decoding of the dynamically generated flag.

[Solution script](./solve/solve.py)

> Flag: `CSCTF{hash-that-changes-every-5-minutes}`

