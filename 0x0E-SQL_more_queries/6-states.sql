-- script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_od_usa;
USE hbtn_od_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
	);
