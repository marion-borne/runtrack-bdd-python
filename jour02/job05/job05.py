import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mars1993",
    database="LaPlateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT superficie FROM etage")

results = cursor.fetchall()

total_superficie = 0
for superficie in results:
    total_superficie += superficie[0]
    
print(f"La superficie de la Plateforme est de {total_superficie} m2")

cursor.close()
mydb.close()