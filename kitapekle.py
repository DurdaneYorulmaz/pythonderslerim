kitapliste = list()
menü = """
1) Kitap Ekle
2) Kitap Çıkar
3) Kitapları Göster
Q) Çıkış
"""
def kitapekle(liste,kitap):
    liste += kitap
    print("Kitap Eklendi!")
    input("Ana menüye dönmek için enter'a basınız!")
def kitapçıkar():
    pass
def listele(liste):
    for a in liste:
        print("Kitap Adı  >>>>>>>", a )
        input("Ana menüye dönmek için enter'a basınız! ")
def cıkıs():
    quit()
while True:
    print(menü)
    secim = input("Seçiminiz :")
    if secim=="1":
        kitapadı = input("Kitap Adı : ")
        kitapekle(kitapliste,kitapadı)
    elif secim=="2":
        kitapçıkar()
    elif secim=="3":
        listele(kitapliste)
    elif secim=="Q" or secim=="q":
        cıkıs()
    else:
        print("Hatalı Girdiniz!")
        input("Ana menüye dönmek için enter'a basınız!")










