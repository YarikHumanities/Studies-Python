from math import sqrt
a=float(input("Значення першого катета: "))
c=float(input("Значення гіпотенузи: "))
b=(c**2-a**2)**0.5
if a>0 and b>0:
    print(b)
elif a<=0:
        print("Значення першого катета недопустиме ")
elif c<=0:
        print("Значення гіпотенузи недопустиме")