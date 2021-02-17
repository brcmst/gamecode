#f = open("oku.txt","r") ------- bulundugum dizindeki dosyayı okumak için r modunu girdim
#mod yazmazsak varsayılan 'r'dir.. okuma modudur------open("yeni.txt")


#1.yöntem------for döngüsü ile...
f = open("oku.txt","r",encoding = "utf-8") #utf-8 ile türkçe karakterler de okunur

for i in f:
    print(i)
f.close()


print("\n")

#2.yöntem-------read fonksiyonu ile...
f = open("oku.txt","r",encoding = "utf-8")

oku = f.read()
print("okunanlar:")
print(oku)
f.close()


print("\n")


#3.yöntem------readline fonksiyonu ile...
#her çağrılışta 1 satır okur
f = open("oku.txt","r",encoding = "utf-8")

print(f.readline())
print(f.readline()) #2 defa çağırdık, 2 satır okudu
f.close()


print("\n")

#4.yöntem------readlines fonksiyonu ile...
#her satırı okuyarak listeye atar. listeden her satır okunabilir
f = open("oku.txt","r",encoding = "utf-8")

liste = f.readlines()
print(liste)
f.close()

















