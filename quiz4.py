
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


