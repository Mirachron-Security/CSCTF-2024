# Double Trouble
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
This challenge combines Morse code and binary encoding.
You'll decode a sequence where Morse symbols are shown in binary:
dots as zeros and dashes as ones. Unravel it to find the flag.
```

<br>

## Requirements
- Decoding

<br>

## Solve
Decode the given sequence with these steps:
1. **Binary to Morse:** Convert `0` to dots (`.`) and `1` to dashes (`-`).
2. **Morse to Text:** Translate Morse code to the original message.

<br>

A CyberChef recipe can help decode the binary-coded Morse quickly. 

Here's a useful [CyberChef link]("https://gchq.github.io/CyberChef/#recipe=To_Morse_Code('-/.','Space','Forward%20slash')Find_/_Replace(%7B'option':'Regex','string':'/'%7D,'%20',true,false,true,false)Find_/_Replace(%7B'option':'Simple%20string','string':'.'%7D,'0',true,false,true,false)Find_/_Replace(%7B'option':'Simple%20string','string':'-'%7D,'1',true,false,true,false)&input=SGVsbG8gdGhlcmUhIFlvdSB3b3JrZWQgaGFyZCBmb3IgdGhpcyBmbGFnLCBzbyB0aGVyZSB5b3UgaGF2ZSBpdDogQ1NDVEZ7YjA3aF9tMHI1M19jMGQzXzRuZF9iMW40cnlfdTUzXzBubHlfMl9jaDRyNGM3M3I1fQ") for this task.

<br>

> Flag: `CSCTF{b07h_m0r53_c0d3_4nd_b1n4ry_u53_0nly_2_ch4r4c73r5}`
