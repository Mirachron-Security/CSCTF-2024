# Onions
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Extract a TOR address and use steganography to extract the flag from hidden images.
```

<br>

## Requirements
- EXIF data inspection
- Steganography tools usage
- TOR navigation

<br>

## Solve
The challenge's name should take you to T O R, or "The Onion Router".

Extract the EXIF data for hidden information. 
```bash
exiftool the_onion_resolver.png
```

A comment shows the domain you have to access. <br>
Install the TOR browser and navigate to the onion link provided in the EXIF data.
```bash
sudo apt install torbrowser-launcher
torbrowser-launcher
```

Analyze the website's image using steganalysis.

The tool `stegseek` uses a dictionary attack to try different passwords against a given image.
```bash
stegseek onion.jpg
```

Do the same for the new file and get the password `onion`.

Now, you can view the file `onion.txt` that contains the flag.

<br>

> Flag: `CSCTF{3x7r4_l4y3r5_0f_53cur17y}`
