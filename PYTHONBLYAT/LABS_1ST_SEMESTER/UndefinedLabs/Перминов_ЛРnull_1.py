import math
def s1 (a):
    return a**2
def s2 (a,b,c,p):
    return (p*(p-a)*(p-b)*(p-c))**0.5
def s3 (a):
    return math.pi*a**2
print('Выберите фигуру: квадрат(1), тругольник(2), круг(3)')
a=int(input('Введите число от 1 до 3, соответствующее каждой из фигур'))
if a == 1:
    c=int(input('Введите сторону квадрата'))
    print(s1(c))
if a == 2:
    a=int(input('Введите первую сторону'))
    b=int(input('Введите вторую сторону'))
    c=int(input('Введите третью сторону'))
    p=((a+b+c)/2)
    print(s2(a,b,c,p))
if a == 3:
    R=int(input('Введите радиус'))
    print(s3(R))
