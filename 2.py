import sqlite3
 db = sqlite3.connect("veritabanı.db")

veriler = [
    (12,45,89)
    (45,68,72)
    (65,23,74)
    (75,68,42)
]
imlec = db.cursor()
imlec.execute("create table ıf not exists 'hayat bos' (yas,kilo,boy)")
for veri in veriler:
    imlec.execute("ınsert into 'oyuncular' values (?,?,?)",veri)
db.commit()

db.close()