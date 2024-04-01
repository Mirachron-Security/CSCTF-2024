#!/bin/bash

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

/usr/bin/socat tcp-listen:9999,reuseaddr,fork exec:./main,rawer,pty,echo=0