#sorted fonk. dizi içindeki elemanları min-max ya da max-min sıralar
#varsayılan min-max sıralamadır

x = [1,22,3,76,48]
print(sorted(x))

print(sorted(x,reverse = True))
#reverse parametresi varsayılan false'dir
#bu durumda min-max sıralar
#reverse = False yaparak max-min sıralanabilir


y = "sırala"
print(sorted(y))
#karakterleri de sözlükteki sıraya göre sıralar
