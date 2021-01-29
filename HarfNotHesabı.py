print("""         ***********************
         Harf notu hesabı
         ***********************""")


#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#90-100	AA	4,00	Başarılı                      # 
#85-89	BA	3,50	Başarılı                      #
#80-84	BB	3,00	Başarılı                      #
#75-79	CB	2,50	Geçer                         #
#70-74	CC	2,00	Geçer                         #
#65-69  	DC	1,50	Koşullu Geçer         #
#60-64	DD	1,00	Koşullu Geçer                 #
#50 ve altı 	FD	0,50	Başarısız- Kalır      #
#                                                     #
#                                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
#if elif else kullanımı..
#vize %30, final %70 etki edecektir.

vize = int(input("vize notu: "))
final = int(input("final notu: "))
n_ort = (vize * 0.3) + (final * 0.7)
print("Ortalamanız :",n_ort)


if(n_ort >= 90):
    print("Harf notunuz AA")
elif(n_ort >= 85):
    print("Harf notunuz BA")
elif(n_ort >= 80):
    print("Harf notunuz BB")
elif(n_ort >= 75):
    print("Harf notunuz CB")
elif(n_ort >= 70):
    print("Harf notunuz CC")
elif(n_ort >= 65):
    print("Harf notunuz DC")
elif(n_ort >= 60):
    print("Harf notunuz DD")
else:
    print("Başarısız..")



