rehber = {
    "kisi1": {
        "cep": "123456789",
        "iş": "123456789",
        "ev": "123456789"
    },
    "kisi2": {
        "cep": "113456788",
        "iş": "113456788",
        "ev": "113456788"
    }
          }
isimler = rehber.keys()
kisi = input("kişi adı : ")
tel = input("istediğiniz telefon : ")
if kisi in isimler:
    flag = True
else:
    flag = False
if flag:
    print(rehber.get(kisi).get(tel,"istediğiniz bilgi mevcut değil!"))
    input("ana menüye dönmek için enter'a basın!")
else: print("aradığınız kişi bulunamadı!")
input("ana menüye dönmek için enter'a basın!")

