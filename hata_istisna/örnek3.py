#
#Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın.
#Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün.
#Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın.
#Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın
#ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
#

def tekMi(x):
    if(x % 2 == 1):
        return x
    else:
        raise ValueError
        

liste = [1,2,3,4,5,6,7,22,43,65,38]


for i in liste:
    try:    
        print(tekMi(i))
    except ValueError:
        pass

    
   
    
        
