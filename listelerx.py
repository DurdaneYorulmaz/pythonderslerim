listeler = ["losAngeles","washington","texas","newyork"]
for a in listeler:
    print(a)
    giris = input("eyalet ekleyin :")

    listeler += [giris]

    for b in listeler:
        print(b)