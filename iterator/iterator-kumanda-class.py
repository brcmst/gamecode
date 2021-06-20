#iter sınıfı olusturma
#__iter()__  ve __next()__  metodlarını tanımlamak gerek

class Kumanda():
    def __init__(self, kanallar):
        self.kanallar = kanallar
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if (self.index < len(self.kanallar)):
            return self.kanallar[self.index]
        else:
            self.index = -1
            raise StopIteration



kumanda = Kumanda(["a","b","c"])
ıterator3 = iter(kumanda)
print(next(ıterator3))
print(next(ıterator3))
print(next(ıterator3))

            
            
        
