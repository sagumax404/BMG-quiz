"""
Kullanıcının girdiği bir değere göre çarpım tablosu oluşturan programı kodlayınız. 
"""
sayi = int(input("Kaçlar tablosu yapılacak:"))
for s in range(0,11):
    samet = sayi*s
    print("{}x{}={}".format(sayi,s,samet))
    
    
