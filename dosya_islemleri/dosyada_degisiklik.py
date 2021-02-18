#dosyanın başında değişiklik yapmak----
with open("oku.txt","r+") as f:#r+ ile hem okuma hem yazma yapılır
    eski = f.read() #dosya okundu
    f.seek(0)
    f.write("yeni\n" +eski) #dosyanın başına gidip 'yeni' yazdırdım
    
  
#dosyanın sonuna veri eklemek-----
with open("oku.txt","a") as ff:
    ff.write("\nAslan Pınar")
    ff.read()



#dosyanın herhangi bir yerine veri eklemek---
with open("oku.txt","r+") as f:
    liste = f.readlines()
    liste.insert(3,"yeni veri\n")
    f.seek(0)
    f.writelines(liste)
