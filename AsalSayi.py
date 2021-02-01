####################
# asal sayı hesabı #
####################

#Sadece kendisine ve 1 sayısına kalansız bölünebilen 1'den büyük pozitif tam sayılardır



def fonksiyon(sayi):

    for i in range(2,sayi): 
        if (sayi % i == 0):  #sayının 2 den sayıya kadar olan sayıyla modu
            return False  #sıfır ise false döndür
    return True   #değilse true döndür
            
                
print("çıkmak için 'a'ya basınız..")

while True:
    sayi = input("sayı giriniz: ")

    if sayi == "a":
        print("çıkış yapılıyor..")
        break
    sayi = int(sayi)
    if sayi == 1:      #sayı 1 ise asal değil
        print("asal sayı değil.")
    elif sayi == 2:     #sayı 2 ise asal
        print("asal sayı..")

    else:
        
        if fonksiyon(sayi):
            print("asal sayı..")
        else:
            print("asal sayı değil.")
            
            
        
            
            
    
