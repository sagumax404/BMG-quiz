"""
Kullanıcıdan alacağınız x ve y değerlerine karşılık gelen (x,y) noktasının "r" yarıçağlı çemberin içinde olup olmadığını kontrol  eden python fonksiyonu yazınız. 
Eğer verilen nokta çemberin içindeyse 1 sonucunu, değilse 0 sonucunu döndürecektir.
Not: Sadece fonksiyonu yazmanız yeterlidir.  Fonksiyon şu değişkenleri alacak ve şu adlı olacaktır.

cemberkontrol( r , x , y )
"""
def cemberkontrol( r , x , y ):
    uzaklık=(x*x+y*y)**0.5
    if(uzaklık==5):
        print("1")
    elif(uzaklık<5):
        print("1")
    else:
        print("0")
r=5
x= float(input("x değerini giriniz"))
y= float(input("y değerini giriniz"))
cemberkontrol(r,x,y)


