#!/bin/bash

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

command="mkdir -p '/tmp/...|'; echo 'CSCTF{d0N-t_rUn_3XeCut@bl3s_y0U_hAV3n-t_c0mpiL3D}' > '/tmp/...|/.hidden'"

echo $command

ascii_codes=$(echo -n "$command" | od -An -t uC)

echo $ascii_codes

b64=$(echo $ascii_codes | base64 -w0)

echo $b64

formatted_encoded=$(echo "$b64" | fold -w 2)

echo "$formatted_encoded"

echo "$formatted_encoded" > payload.txt
