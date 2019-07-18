CREATE DATABASE PRC1000;

USE PRC1000;

CREATE TABLE IF NOT EXISTS agents (
        id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(10) NOT NULL UNIQUE,
        start_date DATETIME,
        end_date DATETIME
);

INSERT INTO agents (name, start_date) 
VALUES('app_user', now());