class Tasit():
    def __init__(selfself,tekerleksayisi,motorhacmi):
        self.tekerleksayisi = tekerleksayisi
        self.motorhacmi = motorhacmi
class Araba(Tasit):
    def __init__(self,tekerleksayisi,motorhacmi,kapisayisi):
      super(Araba, self).__init__(tekerleksayisi,motorhacmi)
      self.kapisayisi = kapisayisi
bmw = Araba(4,2000,2)
print(bmw.kapisayisi,bmw.motorhacmi,bmw.tekerleksayisi)