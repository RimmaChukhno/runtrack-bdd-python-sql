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


cursor.execute("SELECT SUM(superficie) FROM etage;")


result = cursor.fetchone()


if result:
    superficie_totale = result[0]
    print(f"La superficie de La Plateforme est de {superficie_totale} m2")
else:
    print("Aucune superficie trouvée.")


cursor.close()
mydb.close()
