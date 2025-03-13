mysql> SELECT * FROM etage;
+----+-----+--------+------------+
| id | nom | numero | superficie |
+----+-----+--------+------------+
|  1 | RDC |      0 |        500 |
|  2 | R+1 |      1 |        500 |
+----+-----+--------+------------+
2 rows in set (0.00 sec)

mysql> SELECT * FROM salle;
+----+--------------+----------+----------+
| id | nom          | id_etage | capacite |
+----+--------------+----------+----------+
|  1 | Lounge       |        1 |      100 |
|  2 | Studio Son   |        1 |        5 |
|  3 | Broadcasting |        2 |       50 |
|  4 | Bocal Peda   |        2 |        4 |
|  5 | Coworking    |        2 |       80 |
|  6 | Studio Video |        2 |        5 |
+----+--------------+----------+----------+
6 rows in set (0.01 sec)

mysql> notee;
