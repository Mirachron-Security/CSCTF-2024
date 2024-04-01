-- Create the user_data database if it doesn't exist
CREATE DATABASE IF NOT EXISTS user_data;
USE user_data;

-- Create the users table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    real_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(255),
    address VARCHAR(255),
    country VARCHAR(255),
    hashed_password VARCHAR(255),
    secret VARCHAR(255)
);

-- Drop the remote_reader user if it exists
DROP USER IF EXISTS 'remote_reader'@'%';

-- Create the remote_reader user to access tables remotely
CREATE USER 'remote_reader'@'%' IDENTIFIED BY 'reader_password';
GRANT SELECT ON user_data.users TO 'remote_reader'@'%';

-- OLD VERSION of MySQL - Set root user's password for both 127.0.0.1 and localhost
-- ALTER USER 'root'@'localhost' IDENTIFIED BY 'astrongrootpassword';
-- ALTER USER 'root'@'127.0.0.1' IDENTIFIED BY 'astrongrootpassword';

-- Drop the root from 127.0.0.1 if it exists
DROP USER IF EXISTS 'root'@'127.0.0.1';

-- NEW VERSION of MySQL - Set root user's password for both 127.0.0.1 and localhost
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'astrongrootpassword';
CREATE USER 'root'@'127.0.0.1' IDENTIFIED BY 'astrongrootpassword';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'127.0.0.1' WITH GRANT OPTION;

-- Ensure root user access is restricted to localhost and 127.0.0.1
DELETE FROM mysql.user WHERE user = 'root' AND host NOT IN ('localhost', '127.0.0.1');

-- SAVE CHANGES
FLUSH PRIVILEGES;
