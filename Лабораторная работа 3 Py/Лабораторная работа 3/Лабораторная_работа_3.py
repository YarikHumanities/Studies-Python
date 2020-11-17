from math import fabs
x=float(input("Введите значение x: "))
if fabs(x)<1:
    e=float(input("Введите значение точности eps: "))
    n=0
    yp=((-1)**n)*((x**(2*n+1))/(2*n+1))
    s=yp
    while True:
        n=n+1
        yn=((-1)**n)*((x**(2*n+1))/(2*n+1))
        res=yn-yp
        yp=yn
        s+=yp
        if fabs(res)>e:
            break
    print(s)

else:
    print("Значение x недопустимо")