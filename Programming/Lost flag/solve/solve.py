#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import os
import re
from PIL import Image
import pyzbar.pyzbar as pyzbar

# Parameters
n = 50
qr_size = 100
image_path = 'files/qr_image.png' 

# Function to decode a QR code
def decode_qr_code(qr_image):
    decoded_data = pyzbar.decode(qr_image)
    return decoded_data[0].data.decode() if decoded_data else None

def is_hex_string(s):
    match = re.match(r"CSCTF{([0-9A-F]{17})}", s)
    return bool(match)

# Load the large QR code image
large_image = Image.open(image_path)

# Process each QR code
for row in range(n):
    for col in range(n):
        qr_image = large_image.crop((col * qr_size, row * qr_size, (col + 1) * qr_size, (row + 1) * qr_size))

        decoded_string = decode_qr_code(qr_image)

        if not is_hex_string(decoded_string):
            print(f"QR Code at ({row+1}, {col+1}): {decoded_string}")
        # else:
        #     print(decoded_string)
