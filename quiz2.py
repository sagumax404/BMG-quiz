"""
Python'da liste yapılarını kullanarak 5 adet il adı içeren bir liste oluşturunuz.
Kullanıcıdan bir adet sayı alınız. Kullanıcıdan girilen sayı listenin kaçıncı elemanına denk geliyorsa bu ilin ilk 2 ve son 2 karakterini ekrana basacak bir program yazınız. 
Örneğin listemizdeki ilk il "istanbul" olsun. Kullanıcıdan aldığımız sayı 0 ise ekrana İstanbul ilinin ilk 2 ve son 2 harfini alarak ekrana "İsul" yazacak. 
Özetle kullanıcı 0,1,2,3,4 rakamlarından birini girmiş ise bu rakamlara karşılık gelen il adının ilk 2 ve son 2 harfi ekrana yazılacaktır. 
"""
iller = ["Ankara","Bolu","Bursa","Adana","Istanbul"]
sayi = int(input("Bir sayi giriniz:"))
print(iller[sayi][0:2]+iller[sayi][-2:])

