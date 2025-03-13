import mysql.connector
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

class ZooManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="zoo"
        )
        self.cursor = self.conn.cursor()

    def get_nombre_animaux_dans_cage(self, id_cage):
        """Retourne le nombre d'animaux dans une cage donnée."""
        query = "SELECT COUNT(*) FROM animal WHERE id_cage = %s"
        self.cursor.execute(query, (id_cage,))
        return self.cursor.fetchone()[0]

    def get_capacite_max_cage(self, id_cage):
        """Retourne la capacité maximale d'une cage."""
        query = "SELECT capacite_max FROM cage WHERE id = %s"
        self.cursor.execute(query, (id_cage,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def ajouter_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        self.cursor.execute(query, (superficie, capacite_max))
        self.conn.commit()
        print("Cage ajoutée avec succès !")

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        capacite_max = self.get_capacite_max_cage(id_cage)
        if capacite_max is None:
            print("Erreur : La cage spécifiée n'existe pas.")
            return

        nombre_animaux = self.get_nombre_animaux_dans_cage(id_cage)
        if nombre_animaux >= capacite_max:
            print("Erreur : La cage est pleine, impossible d'ajouter l'animal.")
            return

        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (nom, race, id_cage, date_naissance, pays_origine))
        self.conn.commit()
        print("Animal ajouté avec succès !")

    def animal_existe(self, animal_id):
        """Vérifie si un animal existe dans la base de données."""
        query = "SELECT COUNT(*) FROM animal WHERE id = %s"
        self.cursor.execute(query, (animal_id,))
        return self.cursor.fetchone()[0] > 0

    def supprimer_animal(self, animal_id):
        if not self.animal_existe(animal_id):
            print("Erreur : L'animal avec cet ID n'existe pas.")
            return

        query = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(query, (animal_id,))
        self.conn.commit()
        print("Animal supprimé avec succès !")

    def modifier_animal(self, animal_id, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
        if not self.animal_existe(animal_id):
            print("Erreur : L'animal avec cet ID n'existe pas.")
            return

        updates = []
        params = []

        if nom:
            updates.append("nom = %s")
            params.append(nom)
        if race:
            updates.append("race = %s")
            params.append(race)
        if id_cage:
            capacite_max = self.get_capacite_max_cage(id_cage)
            if capacite_max is None:
                print("Erreur : La cage spécifiée n'existe pas.")
                return
            nombre_animaux = self.get_nombre_animaux_dans_cage(id_cage)
            if nombre_animaux >= capacite_max:
                print("Erreur : La cage est pleine, impossible de déplacer l'animal.")
                return
            updates.append("id_cage = %s")
            params.append(id_cage)
        if date_naissance:
            updates.append("date_naissance = %s")
            params.append(date_naissance)
        if pays_origine:
            updates.append("pays_origine = %s")
            params.append(pays_origine)

        params.append(animal_id)
        query = f"UPDATE animal SET {', '.join(updates)} WHERE id = %s"
        self.cursor.execute(query, params)
        self.conn.commit()
        print("Animal modifié avec succès !")

    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        animaux = self.cursor.fetchall()
        for animal in animaux:
            print(f"ID: {animal[0]}, Nom: {animal[1]}, Race: {animal[2]}, Cage: {animal[3]}, Date de Naissance: {animal[4]}, Pays: {animal[5]}")

    def afficher_animaux_par_cage(self):
        query = """
        SELECT a.nom, a.race, c.id AS cage_id, c.superficie, c.capacite_max
        FROM animal a
        LEFT JOIN cage c ON a.id_cage = c.id
        """
        self.cursor.execute(query)
        animaux = self.cursor.fetchall()
        for animal in animaux:
            print(f"Nom: {animal[0]}, Race: {animal[1]}, Cage ID: {animal[2]}, Superficie: {animal[3]}, Capacité Max: {animal[4]}")

    def superficie_totale(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        total = self.cursor.fetchone()[0]
        print(f"La superficie totale du zoo est de {total} m².")

    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()

# Interface utilisateur
def menu():
    zoo = ZooManager()
    while True:
        print("\n=== Gestion du Zoo ===")
        print("1. Ajouter une cage")
        print("2. Ajouter un animal")
        print("3. Supprimer un animal")
        print("4. Modifier un animal")
        print("5. Afficher tous les animaux")
        print("6. Afficher les animaux par cage")
        print("7. Calculer la superficie totale des cages")
        print("8. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            superficie = float(input("Superficie de la cage : "))
            capacite_max = int(input("Capacité maximale de la cage : "))
            zoo.ajouter_cage(superficie, capacite_max)

        elif choix == "2":
            nom = input("Nom de l'animal : ")
            race = input("Race de l'animal : ")
            id_cage = int(input("ID de la cage : "))
            date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
            pays_origine = input("Pays d'origine : ")
            zoo.ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)

        elif choix == "3":
            animal_id = int(input("ID de l'animal à supprimer : "))
            zoo.supprimer_animal(animal_id)

        elif choix == "4":
            animal_id = int(input("ID de l'animal à modifier : "))
            nom = input("Nouveau nom (laisser vide pour ne pas changer) : ") or None
            race = input("Nouvelle race (laisser vide pour ne pas changer) : ") or None
            id_cage = input("Nouvelle cage (laisser vide pour ne pas changer) : ") or None
            date_naissance = input("Nouvelle date de naissance (YYYY-MM-DD) : ") or None
            pays_origine = input("Nouveau pays d'origine (laisser vide pour ne pas changer) : ") or None
            zoo.modifier_animal(animal_id, nom, race, id_cage, date_naissance, pays_origine)

        elif choix == "5":
            zoo.afficher_animaux()

        elif choix == "6":
            zoo.afficher_animaux_par_cage()

        elif choix == "7":
            zoo.superficie_totale()

        elif choix == "8":
            print("Fermeture du programme...")
            zoo.fermer_connexion()
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()
