CREATE DATABASE PRC10000;
DROP DATABASE PRC10000;
SHOW DATABASES;

USE PRC10000;

CREATE TABLE application (
        id INT(11) NOT NULL AUTO_INCREMENT, 
        app_name VARCHAR(50) NOT NULL, 
        app_key VARCHAR(100) NOT NULL, 
        app_secret VARCHAR(100) NOT NULL, 
        description VARCHAR(200) NULL,
        status TINYINT(1) DEFAULT 0, 
        registered_date DATETIME,
        updated_date DATETIME,
        PRIMARY KEY(id)
);

INSERT INTO application (app_name, app_key, app_secret, registered_date, updated_date) 
VALUES('test_app', 'key123', 'secret123', now(), now());

UPDATE application SET app_secret = concat(app_secret, '_closed') WHERE id = 1 AND app_key = 'key123' AND app_name = 'test_app';