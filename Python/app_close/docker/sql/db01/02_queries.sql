CREATE DATABASE PRC1;

USE PRC1;

CREATE TABLE IF NOT EXISTS agents (
        id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(10) NOT NULL UNIQUE,
        start_date DATETIME,
        end_date DATETIME
);

INSERT INTO agents (name, start_date) 
VALUES('test_app1', now());
INSERT INTO agents (name, start_date) 
VALUES('user1', now());
INSERT INTO agents (name, start_date) 
VALUES('user2', now());

CREATE DATABASE PRC2;

USE PRC2;

CREATE TABLE IF NOT EXISTS agents (
        id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(10) NOT NULL UNIQUE,
        start_date DATETIME,
        end_date DATETIME
);

INSERT INTO agents (name, start_date) 
VALUES('user1', now());
INSERT INTO agents (name, start_date) 
VALUES('test_app1', now());
INSERT INTO agents (name, start_date) 
VALUES('user2', now());

CREATE DATABASE PRC3;

USE PRC3;

CREATE TABLE IF NOT EXISTS agents (
        id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(10) NOT NULL UNIQUE,
        start_date DATETIME,
        end_date DATETIME
);

INSERT INTO agents (name, start_date) 
VALUES('user1', now());
INSERT INTO agents (name, start_date) 
VALUES('user2', now());
INSERT INTO agents (name, start_date) 
VALUES('test_app1', now());