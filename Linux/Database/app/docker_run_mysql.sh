#!/bin/bash

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

# Allow to be queries from outside - add comment 
sed -i '31 s/bind-address/#bind-address/' /etc/mysql/mysql.conf.d/mysqld.cnf

# Use port 9999 instead of the default 3306
sed -i 's/3306/9999/' /etc/mysql/mysql.conf.d/mysqld.cnf
sed -i 's/# port/port/' /etc/mysql/mysql.conf.d/mysqld.cnf

usermod -d /var/lib/mysql/ mysql

# Start MySQL
service mysql start

# Create a Database, a user with password, and permissions
mysql -u'root' -p'astrongrootpassword' < start.sql

# Wait for the changes to take place
sleep 5

# Run the main script
/usr/bin/python3 -B main.py -l -p9999

# In case the script fails, the loop keeps going in order to keep the container alive 
while [ true ]; do sleep 60; done
