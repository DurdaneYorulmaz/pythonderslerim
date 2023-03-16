class Asker():
    saglik = 0
    siLah = ' '
    ekipman = ' '
    isim = ' '
    mermi = 0


durdane = Asker()
durdane.saglik = 76
durdane.ekipman = "el bombası"
durdane.siLah = "tüfek"
durdane.mermi = 50
durdane.isim = "Durdane"

b = []
b += ["seyma"]
b += ["hasan"]
print(b)

seyma = Asker()
seyma.saglik = 54
seyma.ekipman = "nükleer bomba"
seyma.siLah = "bıçak"
seyma.mermi = 0
seyma.isim = "Seyma"
print(durdane.isim, durdane.mermi, durdane.siLah, durdane.saglik, durdane.ekipman)
print()
print()
print(seyma.isim, seyma.mermi, seyma.siLah, seyma.saglik, seyma.ekipman)