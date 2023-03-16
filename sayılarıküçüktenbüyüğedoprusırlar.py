liste = ["ankara","istanbul","adana","konya"]
liste2 = liste.copy()
print(liste)
print(liste2)
print(50*"=")

liste.append("mugla")
liste.remove("ankara")
liste2.append("canakkale")
liste2.extend(liste)

print(liste)
print(liste2)
print(50*"=")
liste3 = [1,2,3,7,8,67,78,3,567,4,5,89,9]
liste3.sort()
print(liste3)