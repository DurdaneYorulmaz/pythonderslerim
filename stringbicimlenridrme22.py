isim = input("İsminizi giriniz :")
soy_isim = input("Soy isminizi giriniz :")
hobi = input("Hobilerinizi giriniz :")
felsefe = input("Hayat felsefeniz var ise giriniz : ")

ekrana_basilacak_yazi = """
İsim             : {}
Soy İsim         : {}
Hobileri         : {}
Hayat Felsefesi  : {}
""".format(isim,soy_isim,hobi,felsefe)
print(ekrana_basilacak_yazi)