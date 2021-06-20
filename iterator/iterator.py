#ıterator oluturmak icin __iter()__ ve bu objenin bir sonraki elemanını
#almak icin __next()__ fonk. kullanılır

liste1 = [1,2,3,4,5,6]
print(dir(liste1))   #listenin metodlarını görürüz


iterator = iter(liste1)  #iterator objesi yaratıp içine listeyi göndeririz
print(iterator)        #iteratorü görüntüleriz
print("yukarıdaki iterator")

print(next(iterator))
print("yukarıdaki next ile aldığım ilk liste elemanı ve bu sekilde tum elemanlara erisilir")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
 #print(next(iterator))  #liste elemanı bittiği için bir hata verdi StopIteration

print("***************************")



print("for ornegi")
 #aslında for dongusunde iterator kullanılır
liste2 = [1,2,3,4,5]
for i in liste2:
    print(i)   #biz for döngüsünü böyle görsek de aslında iterator kullanılır

print("pythonın asıl yaptıgı")
#aslında python for yazımı
iterator2 = iter(liste2)
while True:
    try:
        print(next(iterator2))
    except StopIteration:
        break












    
        
    
