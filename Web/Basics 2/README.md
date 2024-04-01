# Basics 2
Author: [Cujbă Mihai](https://www.linkedin.com/in/mihai-cujb%C4%83-109b8a72/)

<br>

## Description
```
Access is filtered based on the User-Agent.
```

<br>

## Requirements
- HTTP requests

<br>

## Solve
Change the User-Agent to contain `NEO`,`X5` and `mini`.

[Here](https://explore.whatismybrowser.com/useragents/explore/operating_platform_string/minix-neo-x5-mini/) is a list of valid User-Agents.

```bash
curl -s http://127.0.0.1:9000 -H 'User-Agent: Mozilla/5.0 (Linux; U; Android 4.2.2; de-at; NEO-X5-mini Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30' | grep CSCTF
```

<br>

> Flag: `CSCTF{UserAgent_whitelist}`