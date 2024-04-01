# {challenge_name}
Author: [Marin Radu](https://github.com/ChronosPK)

## Description
```
Connect to a remote database and find the dynamic flag with a mysql query 
```

## Requirements
- MySQL

## Solve

If you ran this locally, you should firstly get the IP address of your container
```bash
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' linux-database-container
```

```bash
PORT=30050 
HOST="chal.chronossec.site"
mysql -uremote_reader -preader_password -h$HOST -P$PORT user_data -e 'select secret from users where secret like "%CSCTF%";'
```

```bash
mysql -uremote_reader -preader_password -h172.17.0.2 -P3306 user_data -e 'select secret from users where secret like "%CSCTF%";'

+------------------------------------------------------------------------+
| secret                                                                 |
+------------------------------------------------------------------------+
| CSCTF{e3b30153c43adff18f9591389bbdc20e6fcb31b0ae728e0096fc69d1e5e3c4d1} |
+------------------------------------------------------------------------+
```

<br>

> Flag: `CSCTF{hash-that-changes-every-5-minutes}`