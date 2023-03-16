ogrencinin_notu = float(input("lütfen notunuzu giriniz : "))

if ogrencinin_notu >= 85:
    print("takdir almaya hak kazandınız")
elif ogrencinin_notu >=70:
    print("tesekkür belgesi almaya hak kazandınız")
elif ogrencinin_notu < 40:
    print("sınıfta kaldınız!")
else:
    print("sadece sınıfı geçtiniz!")