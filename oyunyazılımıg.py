class Tasit():
    def __init__(self,tekerleksayisi,motorhacmi):
        self.tekerleksayisi = tekerleksayisi
        self.motorhacmi = motorhacmi
class Araba(Tasit):
    pass
bmw = Araba(4,2000)
print(bmw.motorhacmi)