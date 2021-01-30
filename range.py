print("range fonksiyonu")

range(0,20) #sayı dizisi oluşur
print(*range(0,20))

print("***********************")

print(*range(1,20))

print(*range(15)) #başlangıç direkt 0dır

print(*range(1,100,2)) #1den 100e kadar ekrana yaazdırır, 2 atlar

print(*range(5,100,5))

print(*range(0,20,-1)) #1 azaltarak gider

print("*************************")

for i in range(1,100):
    print(i)

    

print("*************************")

for a in range(1,10):
    print("* " *a)
