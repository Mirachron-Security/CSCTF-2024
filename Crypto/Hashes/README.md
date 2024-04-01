# Hashes
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Hash 'CSCTF' with MD5, SHA256 a file, crack a SHA1 hash, then SHA512 a file for the flag.
```

<br>

## Requirements
- Hashing
- Cracking

<br>

## Solve
Execute these steps:

1. **MD5:** Hash 'CSCTF', save to `ctf.txt`.
2. **SHA256:** Hash `ctf.txt` (not needed for the solution).
3. **Crack SHA1:** `6e6a4cd1b4c953e652628742c9bf6e2e9a544b5d`, unnecessary since it's SHA1 :) . Append result to `ctf.txt`.
4. **SHA512:** Hash `ctf.txt` for the final flag.

<br>

Solution [script](./solve/solve.sh)

<br>

> Flag: `CSCTF{66eb9f5349ca95dca65a97c2f3d64fa3611dd79b5c8f8a871c3e1bd5e2ed96ba39ed60061b4f7f694994b039961d1c07c661a80002dd82f5f1ccebc6a057899b}`
