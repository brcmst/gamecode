print("""         ***********************
         python list veri tipi
         ***********************""")

#yeni liste olusturmak
yeniListe = []
yeniListe2 = list()

#olusturdugumuz listlerin tipine bakalım..
print(type(yeniListe))
print(type(yeniListe2))

print("************************")


#yeni bir liste olusturalım..4 elemanlı 3 indisli:
liste1 = ["pazartesi","salı","carsamba","persembe"]

print(liste1) #print ile tüm elemanları yazdırabiliriz.
print(liste1[0]) #köseli parantezle indis no yazarak istediğimiz indisi yazdırabiliriz.


print("append() fonksiyonu ile eleman ekleme: ")
liste1.append("cuma") #append fonk. ile liste sonuna eleman ekleyebiliriz
print(liste1)


print("insert() fonksiyonu ile eleman ekleme: ")
liste1.insert(2,"salı") #insert( , ) fonk. ile istenen indise eleman eklenebilir.
print(liste1)


print("remove() fonksiyonu ile eleman çıkarma: ")
liste1.remove("cuma") #remove fonk. ile istenen değer fonk.a yazılarak çıkarılabilir.
print(liste1)


print("pop() fonksiyonu ile eleman çıkarma: ")
liste1.pop(2) #pop fonk. ile istediğimiz indisteki eleman çıkarılabilir.
print(liste1)


print("reverse() fonksiyonu ile elemanları ters çevirme: ")
liste1.reverse()
print(liste1)


print("max() fonksiyonu ile en büyük değeri bulma(string ifadede alfabetik sıralama): ")
print(max(liste1))

print("min() fonksiyonu ile en küçük değeri bulma(string ifadede alfabetik sıralama): ")
print(min(liste1))



#list veri tipine donusum
print("list veri tipine dönüşüm: ")
x = "burcu" #seklinde stringimiz olsun bunu list tipine donusturmek icin
liste2 = list(x) #liste olusturup x değiskenini içinen yazmamız yeterli
print(liste2)
