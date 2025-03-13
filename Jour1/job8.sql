mysql> SELECT * FROM etudiant WHERE age < 18;
ERROR 1046 (3D000): No database selected
mysql> USE laplateforme;
Database changed
mysql> SELECT * FROM etudiant WHERE age < 18;
+----+--------+--------+------+-------------------------------+
| id | nom    | prenom | age  | email                         |
+----+--------+--------+------+-------------------------------+
|  4 | Barnes | Binkie |   16 | binkie.barnes@laplateforme.io |
+----+--------+--------+------+-------------------------------+
1 row in set (0.00 sec)

mysql> notee;
