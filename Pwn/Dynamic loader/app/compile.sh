#!/bin/bash

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

# Check if shc is installed, if not, install it
if ! command -v shc &> /dev/null; then
    echo "shc is not installed. Installing..."
    sudo apt update
    sudo apt install -y shc
fi

# Check if ../files directory exists, if not, create it
files_directory="../files"
if [ ! -d "$files_directory" ]; then
    echo "$files_directory directory does not exist. Creating..."
    mkdir -p "$files_directory"
fi

# Compile and move the script if shc is installed
if command -v shc &> /dev/null; then
    shc -f vuln.sh
    mv vuln.sh.x vuln
    rm vuln.sh.x.c

    cp vuln "$files_directory"
    echo "vuln copied to $files_directory"
else
    echo "shc is not installed. Unable to compile the script."
fi
