kullanici_adi = input("Kullanıcı adınızı giriniz :")
sifre = input("sifrenizii giriniz:")

belirlenmis_kullanici_adi = "DurdaneNur"
belirlenmis_sifre = "java"

if belirlenmis_kullanici_adi != kullanici_adi:
    print("kullanıcı adınız hatalı!")
elif belirlenmis_sifre != sifre:
    print("sifreniz hatalı!")
else:
    print("giris yaptınız!")