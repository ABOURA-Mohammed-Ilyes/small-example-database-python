import sqlite3

connexion = sqlite3.connect("album.db")
cursor = connexion.cursor()

request = """
CREATE TABLE artise (
artiste_id INTEGER NOT NULL PRIMARY KEY, 
nom VARCHAR 
);
"""

#cursor.execute(request)
connexion.commit()
connexion.close()