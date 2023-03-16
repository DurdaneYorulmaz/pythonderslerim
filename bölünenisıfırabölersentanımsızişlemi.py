a = float(input("bölünen : "))
b = float(input("bölen   : "))
try:
   print("sonuç : ",a/b)
except ZeroDivisionError :
   print("0'a bölüm tanımsızdır!")
except TypeError :
   print("veri tipi hatalı!")
finally:
   print("bu her zaman çalışır!")
