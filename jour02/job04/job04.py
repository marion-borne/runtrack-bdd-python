import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mars1993",
    database="LaPlateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT nom, capacite FROM salle")

results = cursor.fetchall()
for row in results:
    print("Nom:", row[0], "- Capacité:", row[1])

cursor.close()
mydb.close()