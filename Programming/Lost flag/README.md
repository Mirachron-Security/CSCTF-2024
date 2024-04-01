# Lost flag
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Decode multiple QR codes from a single image, filtering out fake flags and identifying the real one.
```

<br>

## Requirements
- Automation
- QR decoding
- Regex

<br>

## Solve
When you decode all the QR codes, you get an endpoint that doesn't exist in my CTF, 
a bunch of fake flags in the form of hex strings, and the flag, rendered only once.

The trick is to separate the real flag from all the fake ones. 
You do this using regex, looking for the pattern of 17 hex chars:
```python
match = re.match(r"CSCTF{([0-9A-F]{17})}", s)
```

[Solution script](./solve/solve.py).

<br>

> Flag: `CSCTF{g0od_ch01c3_budDy}`