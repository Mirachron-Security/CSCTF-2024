#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import qrcode
import random
from PIL import Image

# Parameters 
n = 50  # Number of QR codes per row and column
specific_qr_location = (25, 15) 
flag_contents = "CSCTF{g0od_ch01c3_budDy}" 
obviously_not_the_flag = "https://ctf.chronossec.site/flag-that-nobody-can-ever-find"
qr_size = 100  # Size of each individual QR code in pixels

# Function to generate a random hexadecimal string
def generate_random_hex_string(length):
    return ''.join(random.choices('0123456789ABCDEF', k=length))

# Function to create a QR code
def create_qr_code(data, size):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    return img


# Create a large blank image to hold all QR codes
large_image = Image.new('RGB', (n * qr_size, n * qr_size), 'white')

# Generate and place the QR codes
for row in range(0,n+1):
    for col in range(0,n+1):
        if (row, col) in [(0, 0), (n - 1, 0), (0, n - 1), (n - 1, n - 1)]:
            data = obviously_not_the_flag
        elif (row, col) == specific_qr_location:
            data = flag_contents
        else:
            random_string = generate_random_hex_string(17)
            data = f"CSCTF{{{random_string}}}"
        
        qr_image = create_qr_code(data, qr_size)
        large_image.paste(qr_image, (col * qr_size, row * qr_size))

# Save the final large image
large_image.save('qr_image.png')
