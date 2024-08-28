import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="login"
)

myCusror = db.cursor()
# myCusror.execute("CREATE TABLE User (name varchar(50) NOT NULL, created datetime NOT NULL, passwrd int(4) NOT NULL , id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# db.commit()
# myCusror.execute("CREATE DATABASE login")

# myCusror.execute("INSERT INTO User (name, created, passwrd) VALUES (%s, %s, %s)",("root", datetime.now(), "123"))
# # myCusror.execute("SELECT * FROM Test WHERE name= 'azer_2'")

# myCusror.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")
# db.commit()

# for x in myCusror: 
#     print(x)