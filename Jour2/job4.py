import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"), 
    database="laplateforme"
)

cursor = mydb.cursor()


cursor.execute("SELECT nom, capacite FROM salle;")


results = cursor.fetchall()


print("Liste des salles et leurs capacités :")
for result in results:
    print(f"( {result[0]},  {result[1]}", end=" ) ")


cursor.close()
mydb.close()
