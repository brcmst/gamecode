#sonsuz sayıda isimsiz parametre atamak

def yazdir(*a): # * kullanılır..
    print(a)

yazdir(3,6,7) #gibi daha çok parametre de verilebilir..



#sonsuz sayıda isimli parametre atamak

def yazdiir(**b): #isimli sonsuz parametrede ** kullanılır..
    print(b)

yazdiir(ad = "burcu", sehir = "yalova")
