a = float(input("bölünen : "))
b = float(input("bölen   : "))
try:
   print("sonuç : ",a/b)
except ZeroDivisionError as hata :
   print("0'a bölüm tanımsızdır!")
   print(hata)
except TypeError :
   print("veri tipi hatalı!")
finally:
   print("bu her zaman çalışır!")