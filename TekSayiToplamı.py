####################################
# 1-100 arası tek sayıların toplamı#
####################################

i,toplam = 0,0

while i<100 :
    i = i+1
    if(i % 2 == 1):
        
        toplam += i
    
    else:
        continue
print(toplam)

