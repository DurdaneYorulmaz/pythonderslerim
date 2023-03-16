import sqlite3
db = sqlite3.connect("veritabanı.db")

imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS 'hayat bos' (yas,kilo,boy)")
imlec.execute("INSERT INTO 'oyuncular' VALUES ('32','89','195')")
db.commit()


db.close()