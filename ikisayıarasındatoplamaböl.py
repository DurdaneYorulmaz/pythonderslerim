sayi_1 = float(input("birinci sayıyı giriniz :"))
ifade = input("yapılacak işlmemi giriniz:")
sayi_2 = float(input("ikinci sayıyı giriniz :"))

if ifade == "+":
    print("sonuç :",sayi_1+sayi_2)
elif ifade == "-":
    print("sonuç :",sayi_1-sayi_2)
elif ifade == "*":
    print("sonuç :",sayi_1*sayi_2)
elif ifade == "/":
    print("sonuç :", sayi_1/sayi_2)
    print("Hatalı işlem yaptınız. Program sonlandırıldı.")
