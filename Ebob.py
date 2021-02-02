#################################################
#Kullanıcıdan 2 tane sayı alarak bu sayıların en
#büyük ortak böleni(EBOB) 

def ebob(a,b):
    aebob = set()
    bebob = set()
    

    for i in range(1,a):
        if (a % i == 0):
            aebob.add(i)
        
    for j in range(1,b):
        if (b % j == 0):
            bebob.add(j)
       


    return max(aebob.intersection(bebob))
    

sayi1 = int(input("sayi giriniz: "))
sayi2 = int(input("sayi giriniz: "))
print("ebob: ",ebob(sayi1,sayi2))

    
