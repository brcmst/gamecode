print("""         ***********************
         python tuple veri tipi
         ***********************""")


#yeni bir demet olusturmak için
yeni = ()
type(yeni) #tip olara tuple olduğunuz görürüz


#baska bir yolda tuple() fonk kullanmak
yeni2 = tuple()
type(yeni2)

print("1 2 3 4 5 sayılarından olusan demet : ")
demet = (1,2,3,4,5) #5 elemanlı 4 indisli sayılardan olusan bir demet

len(demet) #tuple eleman sayısı len() fomksiyonu ile bulunabilir

print(demet) #print() ile tuple ı yazdırabiliriz

print("not : tuple veri tipi değiştirilemez, liste tipinde elemanları değiştirebiliyorduk.")

print("********************")

#tek elemanlı tuple olusturmak
demet2 = ("burcu", ) #seklindedir, eğer virgül koymazsak type() ile kontrol ettiğimizde string olacağını görürüz

demet3 = (1,2,"a","b")
print(demet3,"tuple içinde farklı türler olabilir.")

print("********************")

#tuple tipine dönüşüm
x = "merhaba"
demet4 = (tuple(x))
print(demet4)

print("********************")

#tuple içindeki elemanlara ulaşma ve max() min() fonksiyonları
demet5 =(1,2,3,4,5,6,7)
print(demet5)
print(demet5[0],"demetin 1.elemanı")
print(demet5[3],"demetin 3.elemanı")
print(demet5[5],"demetin 5.elemanı") #indis kullanarak elemanlara erisiriz

print(max(demet5),"demetin en büyük elemanı") #max() fonksiyonu
print(min(demet5),"demetin en küçük elemanı") #min() fonksiyonu
