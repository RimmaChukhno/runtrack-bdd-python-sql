mysql> INSERT INTO etudiant (nom, prenom, age, email)
    -> VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM etudiant WHERE nom = 'Dupuis';
+----+--------+----------+------+---------------------------------+
| id | nom    | prenom   | age  | email                           |
+----+--------+----------+------+---------------------------------+
|  5 | Dupuis | Gertrude |   20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis | Martin   |   18 | martin.dupuis@laplateforme.io   |
+----+--------+----------+------+---------------------------------+
2 rows in set (0.00 sec)

mysql> notee;
