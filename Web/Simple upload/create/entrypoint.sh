#!/bin/sh

# Start the clean.sh and generate.sh scripts in the background
/bin/sh /var/www/scripts/clean.sh &
/bin/sh /var/www/scripts/generate.sh &

# Run the PHP built-in server as `ctf` user (least privileges)
su ctf -s /bin/sh -c 'php -S 0.0.0.0:9999 -t /var/www/html'
