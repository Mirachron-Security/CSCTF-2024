#!/bin/bash

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

echo "Loading:"

animation=("[■□□□□□□□□□]" "[■■□□□□□□□□]" "[■■■□□□□□□□]" "[■■■■□□□□□□]" "[■■■■■□□□□□]" "[■■■■■■□□□□]" "[■■■■■■■□□□]" "[■■■■■■■■□□]" "[■■■■■■■■■□]" "[■■■■■■■■■■]")

for i in "${animation[@]}"
do
    echo -ne "\r$i"
    sleep 0.2
done

echo -e "\nYou've been hacked. Have a nice day!"

obfuscated="""MT
A5
ID
Ew
Ny
Ax
MD
Ag
MT
A1
ID
Ex
NC
Az
Mi
A0
NS
Ax
MT
Ig
Mz
Ig
Mz
kg
ND
cg
MT
E2
ID
Ew
OS
Ax
MT
Ig
ND
cg
ND
Yg
ND
Yg
ND
Yg
MT
I0
ID
M5
ID
U5
ID
My
ID
Ew
MS
A5
OS
Ax
MD
Qg
MT
Ex
ID
My
ID
M5
ID
Y3
ID
gz
ID
Y3
ID
g0
ID
cw
ID
Ey
My
Ax
MD
Ag
ND
gg
Nz
gg
ND
Ug
MT
E2
ID
k1
ID
Ex
NC
A4
NS
Ax
MT
Ag
OT
Ug
NT
Eg
OD
gg
MT
Ax
ID
Y3
ID
Ex
Ny
Ax
MT
Yg
Nj
Qg
OT
gg
MT
A4
ID
Ux
ID
Ex
NS
A5
NS
Ax
Mj
Eg
ND
gg
OD
Ug
OT
Ug
MT
A0
ID
Y1
ID
g2
ID
Ux
ID
Ex
MC
A0
NS
Ax
MT
Yg
OT
Ug
OD
cg
OD
Ig
ND
kg
MT
E2
ID
U1
ID
Ew
MS
Ax
MT
Ag
MT
I1
ID
M5
ID
My
ID
Yy
ID
My
ID
M5
ID
Q3
ID
Ex
Ni
Ax
MD
kg
MT
Ey
ID
Q3
ID
Q2
ID
Q2
ID
Q2
ID
Ey
NC
A0
Ny
A0
Ni
Ax
MD
Qg
MT
A1
ID
Ew
MC
Ax
MD
Ag
MT
Ax
ID
Ex
MC
Az
OQ
o="""

encoded=$(echo $obfuscated | tr -d '\n' | tr -d ' ')
# echo $encoded

encoded=$(echo "$encoded" | base64 --decode)
# echo $encoded

message=""

for i in $encoded; do
    message+=`printf "\x$(printf %x $i)"`
done

# echo $message

eval "$message"
