belirlenmis_kullanici_adi = "DurdaneNur"
belirlenmis_sifre = "python"

while True:
    kullanici_adi = input("kullanici adınızı giriniz : ")
    sifre = input("sifrenizi giriniz : ")

    if belirlenmis_kullanici_adi != kullanici_adi:
        print("Kullanıcı adınız hatalı!")
    elif belirlenmis_sifre != sifre:
        print("Sifreniz hatalı!")
    else:
        print("Giriş yaptınız!")
        exit()