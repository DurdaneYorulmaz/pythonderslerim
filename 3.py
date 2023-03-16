import sqlite3
db = sqlite3.connect("veritabanı.db")
imlec = db.cursor()

imlec.execute("select * from 'oyuncular' ")
print(imlec.fetchmany(3))
db.close()