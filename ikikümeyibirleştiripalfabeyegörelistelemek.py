liste = ["ankara","istanbul","adana","konya"]
liste2 = liste.copy()
print(liste)
print(liste2)
print(50*"=")

liste.append("muğla")
liste.remove("ankara")
liste2.append("çanakkale")
liste2.extend(liste)

print(liste)
print(liste2)
print(50*"=")
liste2.sort()
print(liste2)