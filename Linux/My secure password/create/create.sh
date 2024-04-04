#!/bin/bash

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

# Generate a random salt
generate_salt() {
  tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 16
}

# List of users and their passwords
users=('kali' 'user' 'robert' 'chronos' 'knight')
passwords=('jesuslovesme' 'volleyball' 'friends4ever' 'sweetheart' 'manchesterunited')

# Clear files
> passwd
> shadow

# Loop through the users and generate entries
for i in "${!users[@]}"; do
  user="${users[$i]}"
  password="${passwords[$i]}"
  salt=$(generate_salt)
  hash=$(perl -e "print crypt \"$password\", \"\\\$y\\\$j9T\\\$${salt}\\\$\"")
  
  # Generate the passwd and shadow entries
  passwd_entry="$user:x:1001:1001::/home/$user:/bin/bash"
  shadow_entry="$user:$hash:19502:0:99999:7:::"
  
  # Append to files
  echo "$passwd_entry" >> passwd
  echo "$shadow_entry" >> shadow
done

# Add the final files to an archive
zip chall.zip passwd shadow

# Optionally remove passwd and shadow if you don't want them to remain
# rm passwd shadow
