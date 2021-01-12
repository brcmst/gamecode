print("""         ***********************
         python dictionary veri tipi
         ***********************""")

#sözlük olusturmak:
sozluk = {} #süslü parantezlerle yapılabilir
print(type(sozluk)) #class dict olduğunu görürüz

sozluk2 = dict() #dict fonksiyonu ile de sözlük olusturulabilir
print(type(sozluk2))


sozluk3 = {"isim" : "name", "soyisim" : "lastname", "yas" : "age"} #key&value iliskisi vardır

print(sozluk3) #print ile sözlügü yazdırabiliriz

print(sozluk3["soyisim"]) #belli bir elemana ulasmak için anahtarı indis numarası yerine yazarız
print(sozluk3["isim"]) #anahtar yazınca karsılık deger çıktı gelir


sozluk3["sehir"] = "city" #eleman eklemek..
print(sozluk3)


del(sozluk3["isim"]) #del() fonksiyonu ile eleman silinir
print(sozluk3)



liste = ["turuncu", "kırmızı", "mor"] #seklinde bir listemiz olsun, bunu sözlüğe eklemek için
sozluk4 = {"renkler" : liste} #seklinde tanımlarız
print(sozluk4)
