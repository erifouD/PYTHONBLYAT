import math
def m1(a,b,c):
    return 1/2*math.sqrt(2*a**2+2*b**2-c**2)
def m2(a,b,c):
    return 1/2*math.sqrt(2*c**2+2*a**2-b**2)
def m3(a,b,c):
    return 1/2*math.sqrt(2*b**2+2*c**2-a**2)
a = int (input('выберите сторону треугольника'))
b = int (input('выберите сторону треугольника'))
c = int (input('выберите сторону треугольника'))
print (m1(a,b,c))
print (m2(c,a,b))
print (m3(b,c,a))

    


