try:
    x = int(input("birinci sayıyı girin:"))
    y = int(input("ikinci sayıyı girin:"))
    print("bölüm :",x/y)

except ValueError as msj:
    print("sadece sayı girebilirsin....")
    print("hata:",msj)
    raise

finally:
    print("finally bloğu içine yazılan kod her zaman çalışır..")
