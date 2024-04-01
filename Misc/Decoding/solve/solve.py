#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import cv2
import base64

filename = "../files/QR.png"

image = cv2.imread(filename)
detector = cv2.QRCodeDetector()
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

if vertices_array is not None:
	print("QRCode data:\n{}\n".format(data))
else:
	print("There was some error") 
	exit()

string = "".join(chr(int(data[i:i+8],2)) for i in range(0,len(data),8))
print("Binary data:\n{}\n".format(string))

print("Decoding base64 string:")
for i in range(5):
	string = base64.b64decode(string.encode()).decode()
	print(string)
