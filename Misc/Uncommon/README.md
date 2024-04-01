# Uncommon
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Extract digits from an image, extract hidden message, then decode a cipher.
```
<br>

## Requirements
- Image analysis
- Steganography

<br>

## Solve
You get an image with reversed text. 
Analyzing it, you see some digits replacing letters.
Those digits form a password you can use to extract another image.
The second one is an encoded message.
Decoding the message will give you the flag.

<br>
<br>

Use [this tool](https://www.dcode.fr/mirror-writing) to reverse the text. <br>
Extract the digits that form a code: `11372`. <br>
The image has a `PNG` extension but is actually `JPEG`. <br>

Use `steghide` to extract the hidden file with this code. <br>
```bash
steghide extract -sf image.png -p '11372'
```
Output:
```plain
wrote extracted data to "encoded_flag.png".
```

Use [this](https://www.dcode.fr/friderici-windows-cipher) tool to decode the cipher.
You need to specify the character of each number like so:
```python
char(67)char(83)char(67)char(84)char(70)char(80)char(85)char(90)char(90)char(76)char(73)char(78)char(71)char(83)char(79)char(76)char(76)char(85)char(84)char(73)char(79)char(78)
```
<br>

If you copy one of the window images to any text editor, you will see it is just a character before the algorithm transforms it into an image:

![encode and decode](./create/dcode-encode-flag.png)

<br>

> Flag: `CSCTF{puzzling_sollution}`
