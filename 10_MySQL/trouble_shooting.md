MYSQL Trouble Shooting
===

1. Access Denied after initial install of mysql-server
>ERROR 1698 (28000): Access denied for user 'root'@'localhost
Ubuntu 18.04.1 LTS / MySQL Server 5.7.24
```mysql
// access to mysql
sudo mysql
// transaction
BEGIN; 
// check user table
SELECT user, authentication_string, plugin,host FROM mysql.user;
+------------------+-------------------------------------------+-----------------------+-----------+
| user             | authentication_string                     | plugin                | host      |
+------------------+-------------------------------------------+-----------------------+-----------+
| root             |                                           | auth_socket           | localhost |
| mysql.session    | *AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA | mysql_native_password | localhost |
// update root user info
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'YOUR PASSWORD';
// check again
SELECT user, authentication_string, plugin,host FROM mysql.user;
// apply changes
FLUSH PRIVILEGES;
// complete transaction
COMMIT;
// check once again after commit
SELECT user, authentication_string, plugin,host FROM mysql.user;
```
