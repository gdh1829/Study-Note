CREATE DATABASE office;

USE office;

CREATE TABLE IF NOT EXISTS db_info (
        db_name VARCHAR(10) NOT NULL UNIQUE,
        created_date DATETIME
);

INSERT INTO db_info (db_name, created_date) 
VALUES('PRC1000', now());

CREATE TABLE IF NOT EXISTS application (
        id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        app_name VARCHAR(50) NOT NULL, 
        app_key VARCHAR(100) NOT NULL, 
        app_secret VARCHAR(100) NOT NULL, 
        description text NULL,
        status TINYINT(1) DEFAULT 0, 
        registered_date DATETIME,
        updated_date DATETIME
);

CREATE TABLE IF NOT EXISTS user (
        id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        app_id INT(11) NOT NULL,
        company_user_id INT(11) NOT NULL, 
        user_authenticated_id INT(11) NULL,
        company_id INT(11) NULL,  
        registered_date DATETIME,
        updated_date DATETIME,
        FOREIGN KEY fk_app_id(app_id) REFERENCES application(id)
);

CREATE TABLE IF NOT EXISTS user_authenticated (
        id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        user_id INT(11) NOT NULL,
        app_id INT(11) NOT NULL,
        registered_date DATETIME,
        updated_date DATETIME,
        FOREIGN KEY fk_user_id(user_id) REFERENCES user(id),
        FOREIGN KEY fk_app_id(app_id) REFERENCES application(id)
);

-- add new column
ALTER TABLE application ADD company_id INT(11) NULL AFTER id;
-- drop column
-- ALTER TABLE user DROP COLUMN name;
-- change column
ALTER TABLE user CHANGE COLUMN company_id company_id INT(11) NOT NULL;
ALTER TABLE application CHANGE COLUMN app_name app_name VARCHAR(50) NOT NULL UNIQUE;

INSERT INTO application (app_name, company_id, app_key, app_secret, registered_date, updated_date) 
VALUES('test_app1', '1000', 'key123', 'secret123', now(), now());
INSERT INTO application (app_name, app_key, app_secret, registered_date, updated_date) 
VALUES('test_app2', 'key123', 'secret123', now(), now());

INSERT INTO user (app_id, company_id, company_user_id, user_authenticated_id, registered_date, updated_date) 
VALUES('1', '10000', '1', '1', now(), now());
INSERT INTO user (app_id, company_id, company_user_id, user_authenticated_id, registered_date, updated_date) 
VALUES('1', '10001', '1', '1', now(), now());
INSERT INTO user (app_id, company_id, company_user_id, registered_date, updated_date) 
VALUES('1', '10002', '1', now(), now());
INSERT INTO user (app_id, company_id, company_user_id, user_authenticated_id, registered_date, updated_date) 
VALUES('1', '10000', '1', '1', now(), now());

INSERT INTO user_authenticated (user_id, app_id, registered_date, updated_date) 
VALUES('1', '1', now(), now());
INSERT INTO user_authenticated (user_id, app_id, registered_date, updated_date) 
VALUES('2', '1', now(), now());
INSERT INTO user_authenticated (user_id, app_id, registered_date, updated_date) 
VALUES('3', '1', now(), now());
INSERT INTO user_authenticated (user_id, app_id, registered_date, updated_date) 
VALUES('4', '1', now(), now());



UPDATE application SET app_secret = concat(app_secret, '_closed') WHERE id = 1 AND app_key = 'key123' AND app_name = 'test_app';