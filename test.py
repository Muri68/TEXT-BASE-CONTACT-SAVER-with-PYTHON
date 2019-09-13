import sqlite3

with sqlite3.connect("Test.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
lastname VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

cursor.execute("""
INSERT INTO user(username,firstname,lastname,password)
VALUES("test_User","Muri","Isyaku","Abumufida")
""")
db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())
