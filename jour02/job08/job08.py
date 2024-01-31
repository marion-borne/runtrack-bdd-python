import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*********",
    database="zoo"
)

cursor = mydb.cursor()

class Zoo:
    def __init__(self, mydb, cursor):
        self.mydb = mydb
        self.cursor = cursor

    def add_animal(self, nom, race, date_naissance, pays_origine, id_type_cage):
        self.cursor.execute("INSERT INTO animal (nom, race, date_naissance, pays_origine, id_type_cage) VALUES (%s, %s, %s, %s, %s)", (nom, race, date_naissance, pays_origine, id_type_cage))

    def delete_animal(self, id):
        self.cursor.execute("DELETE FROM animal WHERE id = %s", (id,))

    def modify_animal(self, id, nom, race, date_naissance, pays_origine, id_type_cage):
        self.cursor.execute("UPDATE animal SET nom = %s, race = %s, date_naissance = %s, pays_origine = %s, id_type_cage = %s WHERE id = %s", (nom, race, date_naissance, pays_origine, id_type_cage, id))
        
    def add_cage(self, id, superficie, capacite_max, animaux, capacite):
        self.cursor.execute("INSERT INTO cage (id, superficie, capacite_max, animaux, capacite) VALUES (%s, %s, %s, %s, %s)", (id, superficie, capacite_max, animaux, capacite))

    def delete_cage(self, id):
        self.cursor.execute("DELETE FROM cage WHERE id = %s", (id,))

    def modify_cage(self, id, superficie, capacite_max, animaux, capacite):
        self.cursor.execute("UPDATE cage SET superficie = %s, capacite_max = %s, animaux = %s, capacite = %s WHERE id = %s", (superficie, capacite_max, animaux, capacite, id))

    def show_animal(self):
        self.cursor.execute("SELECT * from animal")
        results = self.cursor.fetchall()
        for row in results:  
            print(row)

    def show_cage(self):
        self.cursor.execute("SELECT * from cage")
        results_cage = self.cursor.fetchall()
        for row in results_cage:  
            print(row)
            
    def calculate_total_cage_area(self):
        self.cursor.execute("SELECT SUM(superficie) FROM cage")
        total_area = self.cursor.fetchall()[0][0]
        return total_area

zoo = Zoo(mydb, cursor)

zoo.add_animal('Carbon', 'Chien Boxer', '2017', 'France', 1)
zoo.add_animal('Caramel', 'Chat Exotic Shorthair', '2013', 'Angleterre', 2)
zoo.add_animal('Sesame', 'Chat British Shorthair', '2020', 'Irlande', 3)

zoo.add_cage(1, 20, 2, 1, 2)
zoo.add_cage(2, 10, 1, 2, 1)
zoo.add_cage(3, 15, 3, 3, 3)

print("Liste des animaux :")
zoo.show_animal()
print("Liste des cages :")
zoo.show_cage()

print("Superficie totale des cages :", zoo.calculate_total_cage_area())

cursor.close()
mydb.close()
