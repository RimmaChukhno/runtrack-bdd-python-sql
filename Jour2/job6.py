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


cursor.execute("SELECT SUM(capacite) FROM salle;")


result = cursor.fetchone()


if result and result[0] is not None:
    capacite_totale = result[0]
    print(f"La capacité totale des salles est de : {capacite_totale}")
else:
    print("Aucune capacité trouvée.")


cursor.close()
mydb.close()
