#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

from generate_flag import generate_flag
import base64
from flask import Flask

app = Flask(__name__)

def encode(flag):
    # To binary
    encoded = ''.join(format(ord(i), '08b') for i in flag)
    # To decimal
    encoded = ''.join(str(ord(i)) for i in encoded)
    # To hex
    encoded = ''.join(format(ord(str(i)), "x") for i in encoded)
    # To base64
    encoded = base64.b64encode(encoded.encode()).decode()
    # Reverse
    encoded = encoded[::-1]
    return encoded

@app.route('/')
def serve_flag():
    salt = "3.146416102"
    flag = generate_flag(salt)
    encoded_flag = encode(flag)

    # Debugging
    print("Real flag:", flag)
    # print("Encoded flag:\n" + encoded_flag)

    return encoded_flag

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=False)
