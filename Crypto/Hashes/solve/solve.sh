#!/bin/bash

hash1=$(echo -en "CSCTF" | md5sum | cut -d" " -f1)
echo $hash1

echo $hash1 > ctf.txt

echo '6e6a4cd1b4c953e652628742c9bf6e2e9a544b5d' > hash
john hash -w=/usr/share/wordlists/rockyou.txt

rm hash

hash2=$(echo -en "#winner" | sha1sum | cut -d" " -f1)
echo $hash2 >> ctf.txt

final_hash=$(cat ctf.txt| sha512sum | cut -d" " -f1)
echo "CSCTF{$final_hash}"
