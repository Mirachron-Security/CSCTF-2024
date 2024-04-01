#!/bin/sh

# Infinite loop to regenerate the flag
while true; do
    php /var/www/scripts/generate_flag.php

    # Every 10 seconds
    sleep 10
done
