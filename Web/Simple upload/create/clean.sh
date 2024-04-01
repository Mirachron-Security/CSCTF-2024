#!/bin/sh

# Infinite loop to clean up the uploads directory 
while true; do
    find /var/www/html/uploads ! -name '.hidden' -type f -delete

    # Every 5 minutes
    sleep 300
done
