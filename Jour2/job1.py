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
cursor.execute("SELECT * FROM etudiant;")

results = cursor.fetchall()

print("Liste des etudiant :")
for result in results:
    print(result)

cursor.close()
mydb.close() 