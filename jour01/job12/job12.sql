mysql> INSERT INTO etudiant (prenom, nom, age, email)
    -> VALUES ('Martin', 'Dupuis', 18, 'martin.dupuis@laplateforme.io');

mysql> SELECT * FROM etudiant
    -> WHERE nom IN (
    -> SELECT nom FROM etudiant
    -> GROUP BY nom
    -> HAVING COUNT(*) > 1);