-- T01. Root user
-- Script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH authentication_plugin BY 'user_0d_1_pwd'
GRANT * ON *.* TO user_0d_1@localhost
