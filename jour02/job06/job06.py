import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mars1993",
    database="LaPlateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT capacite FROM salle")

results = cursor.fetchall()

total_capacite = 0
for capacite in results:
    total_capacite += capacite[0]
    
print(f"La capacité de toutes les salles est de : {total_capacite}")

cursor.close()
mydb.close()