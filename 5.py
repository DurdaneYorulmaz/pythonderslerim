import sqlite3
db = sqlite3.connect("veritabanı.db")
imlec = db.cursor()

imlec.execute("select * from 'oyuncular' ")
print(imlec.fetchone())
print(imlec.fetchone())
db.close()