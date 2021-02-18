def harf(puan):

    puan = puan[:-1]#fazladan olan \n silinmiş olur..boşluk gider
    liste = puan.split(",") #her elemana ulaşabilmek için split fonk. kullanılır
    ogrenci = liste[0]
    vize = int(liste[1])
    final = int(liste[2])

    ortalama = (vize*0.3) + (final*0.7)

    if(ortalama >= 90):
        h_not = "AA"
    elif(ortalama >= 85):
        h_not = "BA"
    elif(ortalama >= 80):
        h_not = "BB"
    elif(ortalama >= 75):
        h_not = "CB"
    elif(ortalama >= 70):
        h_not = "CC"
    elif(ortalama >= 65):
        h_not = "DC"
    elif(ortalama >= 60):
        h_not = "DD"
    else:
        h_not = "FF"

    return ogrenci + "----" + h_not + "\n"



with open("ogr_notları.txt","r",encoding="utf-8") as f:
    okunan = []
    for i in f:
        okunan.append(harf(i))
        
    with open("not.txt","w",encoding="utf-8") as ff:
        for i in okunan:
            ff.write(i)
