# WHOis #1
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Find the odd DNS record of my website
```

<br>

## Requirements
- DNS reconnaissance

<br>

## Solve
Choose an (online) tool that shows DNS records for domains.

```bash
dig TXT chronossec.site

; <<>> DiG 9.18.16-1-Debian <<>> TXT chronossec.site
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 61519
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;chronossec.site.			IN	TXT

;; ANSWER SECTION:
chronossec.site.		300	IN	TXT	"CSCTF{wh47_4r3_y0u_l00k1n6_47?}"
chronossec.site.		300	IN	TXT	"v=spf1 include:_spf.mx.cloudflare.net ~all"

;; Query time: 52 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Tue Sep 19 17:20:34 EEST 2023
;; MSG SIZE  rcvd: 143
```

<br>

> Flag: `CSCTF{wh47_4r3_y0u_l00k1n6_47?}`
