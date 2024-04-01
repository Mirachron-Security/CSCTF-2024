#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import base64
import requests

flag = "CSCTF{@nOth3r_h1dd3N_f12g}"
string = f"Not so hard, right? This is the flag:\n{flag}"
nr = 5

# Plain text to base64
def encoding(string,nr):
	for i in range(nr):
		string = base64.b64encode(string.encode()).decode()
	return string

def decoding(string,nr):
	for i in range(nr):
		string = base64.b64decode(string.decode()).encode()
	return string

base64_string = encoding(string,nr)

# Base64 to binary
def tobinary(string):
	string = "".join(format(ord(i),'08b') for i in string)
	return string

binary_string = tobinary(base64_string)

# Binary to QR code
base_url = "https://chart.googleapis.com/chart?cht=qr&chs=500x500&chld=M|1&chl="
url = base_url + binary_string

r = requests.get(url=url)
if r.status_code == 200:
	with open("QR.png","wb") as image:
		image.write(r.content)
else:
	print("Failed to download the image.")

