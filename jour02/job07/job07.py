import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mars1993",
    database="LaPlateforme",
)

cursor = mydb.cursor()

class salarie:
    def __init__(self, cursor):
        self.cursor = cursor
        
    def delete(self):
        self.cursor.execute("DELETE FROM employe WHERE nom = 'Lucas'")
        
    def add(self):
        self.cursor.execute("INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Idriss', 'Bouabdallah', 2800, 18)")
        
    def show(self):
        self.cursor.execute("SELECT * FROM employe")
        results = self.cursor.fetchall()
        for row in results:
            print(row)

salarie = salarie(cursor)
salarie.show()
salarie.delete()
salarie.add()

cursor.close()
mydb.close()