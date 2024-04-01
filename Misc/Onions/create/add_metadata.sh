#!/bin/bash

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#


# hostname=$(docker exec -it misc-onions-container cat /var/lib/tor/hidden_service/hostname)
# hostname=$(kubectl exec -it pod/misc-onions-7f874c9b7c-7rnqf -n haproxy -- cat /var/lib/tor/hidden_service/hostname)
hostname="sxegpfvdhr2fypwdv7do37qse4juwudxl5xejkp2qmpzy4on25hw47yd.onion"

image_path="the_onion_resolver.png"

exiftool -overwrite_original -comment="$hostname" "$image_path"

exiftool "$image_path"

cp "$image_path" "../files/$image_path"

echo -en "\nCopied '$image_path' to ../files"
