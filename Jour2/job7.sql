mysql> CREATE DATABASE company;
ERROR 1007 (HY000): Can't create database 'company'; database exists
mysql> 
mysql> USE company;
Database changed
mysql> 
mysql> CREATE TABLE service (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255) NOT NULL
    -> );
ERROR 1050 (42S01): Table 'service' already exists
mysql> 
mysql> CREATE TABLE employe (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255) NOT NULL,
    ->     prenom VARCHAR(255) NOT NULL,
    ->     salaire DECIMAL(10, 2) NOT NULL,
    ->     id_service INT,
    ->     FOREIGN KEY (id_service) REFERENCES service(id)
    -> );
ERROR 1050 (42S01): Table 'employe' already exists
mysql> INSERT INTO service (nom) VALUES
    -> ('D‚veloppement'),
    -> ('Marketing'),
    -> ('Ressources Humaines'),
    -> ('Finance');
Query OK, 4 rows affected (0.02 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
    -> ('Dupont', 'Jean', 3500, 1),
    -> ('Martin', 'Lucie', 2500, 2),
    -> ('Durand', 'Pierre', 5000, 3),
    -> ('Lemoine', 'Marie', 3200, 4);
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM employe WHERE salaire > 3000;
+----+---------+--------+---------+------------+
| id | nom     | prenom | salaire | id_service |
+----+---------+--------+---------+------------+
|  1 | Dupont  | Jean   | 3600.00 |          1 |
|  3 | Durand  | Pierre | 5000.00 |          3 |
|  4 | Lemoine | Marie  | 3200.00 |          4 |
|  5 | Vidal   | Sophie | 4000.00 |          2 |
|  6 | Dupont  | Jean   | 3500.00 |          1 |
|  8 | Durand  | Pierre | 5000.00 |          3 |
|  9 | Lemoine | Marie  | 3200.00 |          4 |
+----+---------+--------+---------+------------+
7 rows in set (0.00 sec)

mysql> SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS service
    -> FROM employe e
    -> JOIN service s ON e.id_service = s.id;
+----+---------+--------+---------+---------------------+
| id | nom     | prenom | salaire | service             |
+----+---------+--------+---------+---------------------+
|  1 | Dupont  | Jean   | 3600.00 | D‚veloppement       |
|  3 | Durand  | Pierre | 5000.00 | Ressources Humaines |
|  4 | Lemoine | Marie  | 3200.00 | Finance             |
|  5 | Vidal   | Sophie | 4000.00 | Marketing           |
|  6 | Dupont  | Jean   | 3500.00 | D‚veloppement       |
|  7 | Martin  | Lucie  | 2500.00 | Marketing           |
|  8 | Durand  | Pierre | 5000.00 | Ressources Humaines |
|  9 | Lemoine | Marie  | 3200.00 | Finance             |
+----+---------+--------+---------+---------------------+
8 rows in set (0.00 sec)

mysql> notee;
