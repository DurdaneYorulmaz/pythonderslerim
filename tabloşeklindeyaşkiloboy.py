import sqlite3
db = sqlite3.connect("veritabanı.db")

imlec = db.cursor()
imlec.execute("CREATE TABLE oyuncular (yas,kilo,boy)")
db.close()