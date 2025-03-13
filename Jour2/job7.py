import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Employe:
    def __init__(self, id=None, nom=None, prenom=None, salaire=None, id_service=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="company"
        )

    @classmethod
    def create(cls, employe):
        conn = cls.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (employe.nom, employe.prenom, employe.salaire, employe.id_service))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = cls.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM employe"
        cursor.execute(query)
        result = cursor.fetchall()
        employes = []
        for row in result:
            employe = cls(id=row[0], nom=row[1], prenom=row[2], salaire=row[3], id_service=row[4])
            employes.append(employe)
        cursor.close()
        conn.close()
        return employes

    @classmethod
    def update(cls, employe):
        conn = cls.get_connection()
        cursor = conn.cursor()
        query = "UPDATE employe SET nom=%s, prenom=%s, salaire=%s, id_service=%s WHERE id=%s"
        cursor.execute(query, (employe.nom, employe.prenom, employe.salaire, employe.id_service, employe.id))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def delete(cls, employe_id):
        conn = cls.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM employe WHERE id=%s"
        cursor.execute(query, (employe_id,))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def get_high_salary(cls):
        conn = cls.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM employe WHERE salaire > 3000"
        cursor.execute(query)
        result = cursor.fetchall()
        employes = []
        for row in result:
            employe = cls(id=row[0], nom=row[1], prenom=row[2], salaire=row[3], id_service=row[4])
            employes.append(employe)
        cursor.close()
        conn.close()
        return employes

# Exemple 


new_employe = Employe(nom="Vidal", prenom="Sophie", salaire=4000, id_service=2)
Employe.create(new_employe)

# Récupérer et afficher tous les employés
employes = Employe.get_all()
for employe in employes:
    print(f"ID: {employe.id}, Nom: {employe.nom}, Prénom: {employe.prenom}, Salaire: {employe.salaire}, Service: {employe.id_service}")

# Mettre à jour un employé
employe_to_update = Employe(id=1, nom="Dupont", prenom="Jean", salaire=3600, id_service=1)
Employe.update(employe_to_update)

# Supprimer un employé
Employe.delete(2)

# Récupérer les employés avec salaire > 3000
high_salary_employes = Employe.get_high_salary()
for employe in high_salary_employes:
    print(f"ID: {employe.id}, Nom: {employe.nom}, Prénom: {employe.prenom}, Salaire: {employe.salaire}")
