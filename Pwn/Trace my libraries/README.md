# Trace my libraries
Author: [Marin Radu](https://www.linkedin.com/in/radumarin001/)

<br>

## Description
```
Investigate a binary's system call activities to discover hidden function calls and decode the underlying behavior.
```

<br>

## Requirements
- Binary analysis
- `ltrace` utility

<br>

## Solve
Inspect the binary with `ltrace` to trace library calls and spot the concealed operations. 
The binary performs obfuscation which can be reversed to reveal the flag.

```bash
ltrace ./vuln
```

The output from `ltrace` won't immediately show the complete information due to the limited buffer size, 
so adjusting the string size parameter is necessary.

```bash
ltrace -s 100 ./vuln
```

<br>

You can see the initial scripts: <br>
Create the encoded flag: [encode.py](./app/encode.py) <br>
Script before compilation: [vuln.c](./app/vuln.c)

<br>

> Flag: `CSCTF{l3t.s_trAc3_the_libr@r13S_______________________bUT_w3_n3ED_the_bIg.piCtUr3}`



