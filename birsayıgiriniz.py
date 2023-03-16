import random

while True:
    rastgele = random.randint(1,9)

    sayi = int(input("bir sayı giriniz : "))
    if sayi == rastgele:
        print("tebrikler!")
    else:
     input("yeniden oynamak için eneter'a basınız!")