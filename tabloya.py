import sqlite3
db = sqlite3.connect("veritabanı.db")

imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS 'hayat bos' (yas,kilo,boy)")
db.close()