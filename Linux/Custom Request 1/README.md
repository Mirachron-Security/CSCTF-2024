# Custom Request 1
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Follow the server's instructions and append the Python version to the query to retrieve the dynamic flag.
```

<br>

## Requirements
- `curl`
- HTTP requests

<br>

## Solve
Connect to the provided domain and port, read the message, check the Python version, and append it to the query:

```bash
DOMAIN=chal.chronossec.site
PORT=30030

/usr/bin/curl -sI http://$DOMAIN:$PORT | /usr/bin/grep -i python

/usr/bin/curl -s http://$DOMAIN:$PORT/flag?python=3.9.17
```

<br>

> Flag: `CSCTF{hash-that-changes-every-5-minutes}`
