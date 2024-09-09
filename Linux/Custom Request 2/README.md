# Custom Request 2
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Use curl to send a custom request including a query and a special HTTP header
```

<br>

## Requirements
- `curl`
- Custom HTTP headers

<br>

## Solve
Craft a `curl` command with a custom query and header to bypass the server's checks and retrieve the flag:

```bash
DOMAIN="chal.chronossec.site"
PORT=30040

# Get the base64 value of "secret"
secret=$(echo -en "secret" | base64 -w0)

# Get the value of header Content-Type
/usr/bin/curl -v http://$DOMAIN:$PORT
# using -I to get the header will show a different result, 
# because the error is handled by the http.server module

/usr/bin/curl -s http://$DOMAIN:$PORT/$secret?flag=please -H "CSCTF: dc23933049d8b06808e15916d9cc735bd5c82fc87e5f3a970442f6fc04f5a275"
```

<br>

> Flag: `CSCTF{hash-that-changes-every-5-minutes}`
