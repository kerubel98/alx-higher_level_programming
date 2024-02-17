-- script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_od_01'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_od_01'@'localhost';
FLUSH PRIVILEGES;
