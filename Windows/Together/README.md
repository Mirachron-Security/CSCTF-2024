# Together
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Unite multiple archive parts with 7z, then read the flag from a text file.
```

<br>

## Requirements
- `7z`

<br>

## Solve
Open the first zip archive to reveal the `7z` archive parts

Use a standard archiving program like `7z` to unite those archive parts.<br>
Select all the parts and open 7z options to `extract to '*\'`.<br>
This will create a folder with the original contents, among which is the flag.

<img src="./create/archives.png" width="500">

<br>

Of course, you can do it on a Linux system as well:
```bash
unzip -l chall.zip # to verify the contents
unzip chall.zip

7z x archive.zip.001 # 7z will detect automatically the other segments

cat archive/old.txt
```

<br>

> Flag: `CSCTF{unbreakable_s3CreTs_u2ve1l3D}`
