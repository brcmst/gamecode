#write fonksiyonu ile dosyaya yazılır
#önce dosyayı açmak gerekmektedir
#en son da dosyayı close fonksiyonu ile kapamalıyız

ff =open("yaz.txt","w")
ff.write("yeni actigim dosya..\n")
ff.close()


#w modu dosya olusturuyor, zaten dosya varsa silip yenisini olsuturuyor
#a modu ile dosya yoksa olusturulur, varsa dosyaya veri eklemek için kullanılır

fff = open("yaz.txt","a")
fff.write("a modu ile yeni veri ekledim..\n")
fff.close()
#eklenen verileri alt alta yazmak için \n kullanılır
