import random
import os


while True:
    os.system("cls")
    rastgele = random.randint(1,9)

    sayi = int(input("bir sayı giriniz : "))
    if sayi == rastgele:
        print("tebrikler!")
        exit()
    else:
     input("yeniden oynamak için eneter'a basınız!")