mysql> CREATE DATABASE store;
ERROR 1007 (HY000): Can't create database 'store'; database exists
mysql> 
mysql> USE store;
Database changed
mysql> 
mysql> CREATE TABLE category (
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     name VARCHAR(255) NOT NULL
    -> );
ERROR 1050 (42S01): Table 'category' already exists
mysql> 
mysql> CREATE TABLE product (
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     name VARCHAR(255) NOT NULL,
    ->     description TEXT,
    ->     price INT NOT NULL,
    ->     quantity INT NOT NULL,
    ->     id_category INT,
    ->     FOREIGN KEY (id_category) REFERENCES category(id)
    -> );
ERROR 1050 (42S01): Table 'product' already exists
mysql> show tables;
+-----------------+
| Tables_in_store |
+-----------------+
| category        |
| product         |
+-----------------+
2 rows in set (0.01 sec)

mysql> Terminal close -- exit!
