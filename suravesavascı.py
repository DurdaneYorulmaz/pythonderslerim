savascı = { "Güç" : 165,
            "Sp" : 70,

         "STR" : 175,
            "HP" : 4050}
sura = {"Güç": 130,
        "Sp": 160,
       "STR": 40,
            "HP": 2560}
def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["Güç"]
    vurulan["HP"] = vurulan["HP"] - eksilen

input("Vurmak için enter'a basınız!")
vur(savascı,sura)
print("sura'nın canı : ", sura["HP"])
input("Vurmak için enter'a basınız!")
vur(sura,savascı)
print("savascı'nın canı : ", savascı["HP"])