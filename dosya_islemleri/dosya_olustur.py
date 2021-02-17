#open fonksiyonu dosya açmak için kullanılır
#2 parametre alır; 1.dosya adı, 2.mod...
#birinci parametre olarak özel bir yol verilmezse oluşturulan dosya varsayılan python kodu hangi dosyada ise aynı yerde oluşturulur..
#-------open("ornek1.txt","w")------- şeklinde kullanılır
#ilk parametre oluşturulacak dosyanın adı, ikinci p. hangi modda kullanılacağı



f = open("olustur.txt","w") #kontrol edebilmek için değişkene atadık
f.close() #açtığımız dosyayı bu şekil kaparız

f2 = open("C:/baska/ornek2.txt","w") #başka dizinde dosya oluşturmak için dizin yolunu da yazdık ama düz taksim kullanıldığına dikkat ediniz..
f2.close()

