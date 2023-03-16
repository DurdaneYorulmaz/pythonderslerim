import sqlite3
db = sqlite3.connect("veritabanı.db")
imlec = db.cursor()

imlec.execute("select * from 'oyuncular' ")
veriler = imlec.fetchall()
print(veriler)
db.close()