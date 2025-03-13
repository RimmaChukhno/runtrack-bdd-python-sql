mysql> CREATE DATABASE zoo;
Query OK, 1 row affected (0.01 sec)

mysql> 
mysql> USE zoo;
Database changed
mysql> 
mysql> CREATE TABLE cage (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     superficie DECIMAL(10,2) NOT NULL,
    ->     capacite_max INT NOT NULL
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> 
mysql> CREATE TABLE animal (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255) NOT NULL,
    ->     race VARCHAR(255) NOT NULL,
    ->     id_cage INT,
    ->     date_naissance DATE NOT NULL,
    ->     pays_origine VARCHAR(255) NOT NULL,
    ->     FOREIGN KEY (id_cage) REFERENCES cage(id) ON DELETE SET NULL
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> notee;
