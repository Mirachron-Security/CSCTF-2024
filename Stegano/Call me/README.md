# Call me
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Decode 2 telephone number ciphers.
```

<br>

## Requirements
- Telephone number encoding

<br>

## Solve
Extract the text from the image.
```bash
tesseract code.jpg out.txt
```

Use an online tool for [DTMF](https://www.dcode.fr/dtmf-code) to decode the first code.
```
1209-852 1209-852 1209-852 1209-852 1477-770 1336-697 1336-697 1336-697 1336-697 1336-697 1336-697 
1209-770 1209-770 1209-770 1336-852 1336-697 1209-852 1209-852 1477-697 1477-697 1477-697 1477-852 
1477-852 1477-852 1477-770 1477-770 1477-770 1336-852 1336-852 1209-852 1209-852 1209-852 1209-852 
1209-770 1209-770 1477-770 1477-770 1477-770 1477-770 1477-770 1477-697 1477-697
```
```
222 7777 222 8 333 0 444 0 8 2 7 7 33 3 0 999 666 88 777 0 7 44 666 66 33
```

Use another tool like [this one - Multitap ABC](https://www.dcode.fr/multitap-abc-cipher) to decode the second code.

You won't know exactly how the digits are split, so you will have to try based on the flag format.
```
222 7777 222 8 333 0 444 0 8 2 7 7 33 3 0 999 666 88 777 0 7 44 666 66 33
```
```
CSCTF I TAPPED YOUR PHONE
```

The flag is case insensitive.

<br>

> Flag: `CSCTF{I_tapped_your_phone}`