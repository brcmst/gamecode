#liste sıralama, parametresiz fonk. ile

sayi = [1,2,44,34,63]
print(sayi)

def minmax():
    print(sorted(sayi))

def maxmin():
    print(sorted(sayi,reverse= True))

sira = input("liste küçükten büyüğe sıralanması için 1'e, büyükten küçüğe için 2'ye basın")

if sira =="1":
    minmax()
else:
    maxmin()
