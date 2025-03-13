mysql> CREATE TABLE etage (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255) NOT NULL,
    ->     numero INT NOT NULL,
    ->     superficie INT NOT NULL
    -> );
ERROR 1050 (42S01): Table 'etage' already exists

mysql> SHOW TABLES;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etage                  |
| etudiant               |
| salle                  |
+------------------------+
3 rows in set (0.00 sec)

mysql> DESCRIBE etage;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| nom        | varchar(255) | NO   |     | NULL    |                |
| numero     | int          | NO   |     | NULL    |                |
| superficie | int          | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
4 rows in set (0.01 sec)

mysql> DESCRIBE salle;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| nom      | varchar(255) | NO   |     | NULL    |                |
| id_etage | int          | NO   | MUL | NULL    |                |
| capacite | int          | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> notee;
