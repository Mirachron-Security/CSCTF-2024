#!/bin/bash

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

# Get a copy of each original file that will be embedded
cp original-files/* .

# Hide the onion.txt in the small-onion.jpg image
steghide embed -cf small-onion.jpg -ef onion.txt -Z -p "onion"

# embed the earlier small-onion.jpg into the bigger onion.jpg image that will be displayed on the webpage
steghide embed -cf onion.jpg -ef small-onion.jpg -Z -p "onionbreath"

# Copy the cover image to the application
cp onion.jpg ../app

# Clear the directory
rm onion.jpg onion.txt small-onion.jpg