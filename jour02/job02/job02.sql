mysql> CREATE TABLE etage (
    -> id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -> nom VARCHAR(255),
    -> numero INT,
    -> superficie INT );

mysql> CREATE TABLE salle (
    -> id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -> nom VARCHAR(255),
    -> id_etage INT,
    -> capacite INT );