#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

#!/usr/bin/python3

flag = 'CSCTF{l3t.s_trAc3_the_libr@r13S_______________________bUT_w3_n3ED_the_bIg.piCtUr3}'

def deobf(s):
    result = ""
    for i in range(len(s)):
        result += chr(ord(s[i]) ^ (i % 256) ^ 0x80)
    return result

def obf(s):
    result = ""
    for i in range(len(s)):
        result += hex(ord(s[i]) ^ 0x80 ^ (i % 256))

    return result.replace("0x","\\x")

encoded_flag = obf(flag)

with open("flag.enc","w") as file:
    file.write(encoded_flag)
    print(encoded_flag)
