print("""         ***********************
         python set veri tipi
         ***********************""")

#bos kume olusturmak icin set() fonksiyonu kullanılır
yeni = set()
print(type(yeni)) #type fonksiyonu ile baktığımızda set veri tipi oldugunu görürüz


liste = ["a","b","c"] #seklinde listemiz olsun
kume = set(liste) #bu sekilde listeyi kümenin elemanı yapabiliriz
print(kume)


demet = ("d","e","f")
kume1 = set(demet)  #tuple'ı da kümenin elemanı yapabiliriz
print(kume1)


print(""" NOT : sayılardan küme oluşturulmuyor . """)


x = "burcu"
kume2 = set(x) #string veriyi de küme elemanı yapabiliriz
print(kume2)



#birden fazla string dizisi {} ile gönderilebilir
x1 = {"s","e","l","a","m"}
kume3 = set(x1)
print(kume3)


print("NOT : kümeler sırasız bir şekilde eleman tutar, print ile çıktılarına bakarsanız fark edersiniz")

print("NOT : kümeler aynı elemanı bir defa yazar, birleştirme  işlemi.")


#kümeye add()fonksiyonu ile eleman eklenilir
print("add() fonksiyonu")
x2 = "kelime"
kume4 = set(x2)
kume4.add("a") #önce stringi küme elemanı yaptık daha sonra bu kümeye a stringini ekledik
print(kume4)


#kümeden remove() fonksiyonu ile eleman çıkarılır
print("remove() fonksiyonu")
x3 = "deger"
kume5 = set(x3)
kume5.remove("e") #d e g r elemanlarından oluşan kümeden e stringi çıkarılmış olur
print(kume5)


#clear() fonksiyonu ile kümenin tüm elemanları temizlenir
print("clear() fonksiyonu")
liste1 = ["x","y","z"] #şeklinde listemiz olsun
x4 = set(liste1) #listeyi kümeye eleman olarak atadık
print(x4)
x4.clear() #kümedeki elemanların hepsi temizlenir, boş küme kalır
print(x4)



#len() fonksiyonu ile kümedeki eleman sayısını buluruz
print("len() fonksiyonu")
x5 = "fonksiyon"
kume6 = set(x5)
print(kume6)
print(len(kume6)) 



#copy() fonksiyonu ile küme kopyalamak
print("copy() fonksiyonu")
x6 = "kopyalamak"
kume7 = set(x6)
kume8 = kume7.copy() #yeni bir küme oluşturup kume7'nin kopyasını buna atadık
print("NOT : copy() ile küme kopyalayınca, bir kümede yapılan değişiklik diğerini etkilemez. Çünkü ayrı bellek bölgelerinde tutulur.")
print(kume7,"küme7")
print(kume8,"küme8")



#discard() fonksiyonu ile kümeden eleman silmek
print("discard() fonksiyonu")
x7 = "silmek"
kume9 = set(x7)
print(kume9)
kume9.discard("s") #kümeden s stringi silinir
print(kume9)



#pop() fonksiyonu ile eleman silmek
print("pop() fonksiyonu")
kume10 = {9,8,7,6,5}
print(kume10)
kume10.pop()
print(kume10)
print("NOT : pop() fonksiyonu rastgele bir eleman siler")


#iki küme arası fark "-"
print("kümeler arası fark '-' ")
kume11 = {1,2,3,4,5}
kume12 = {3,4,5,6}
print(kume11, "küme11")
print(kume12, "küme12")
print(kume11-kume12) #- ile fark elde edilir



#iki kümenin kesişimi "&"
print("iki kümenin kesişimi '&' ")
print(kume11 & kume12) 


#iki küme birleşimi " | "
print("iki küme birleşimi '|' ")
print(kume11 | kume12)




