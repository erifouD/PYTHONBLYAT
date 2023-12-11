'''import math

def s1(a,b):
    return a*b
def s2(a,b):
    return (b1*b2)*0.5
def s3(a,b,c,p):
    return (p*(p-a)*(p-b)*(p-c))**0.5
def s4(a):
    return math.pi * a**2
print('Выберите фигуру: треугольник(1), квадрат(2), параллелограм(3), прямоугольник(4), круг(5)')

a = int(input('выберите число от 1 до 5, соответствующие каждой из фигур'))

if a == 2 or a == 4:
    c1 = int(input('введите сторону четырёхугольника'))
    c2 = int(input('введите сторону четырёхугольника'))
    print(s1(c1,c2))
if a == 3:
    b1 = int(input('введите высоту фигуры'))
    b2 = int(input('введите сторону фигуры'))
    print(s2(b1,b2))
if a == 1:
    a1 = int(input('введите сторону треугольника'))
    a2 = int(input('введите сторону треугольника'))
    a3 = int(input('введите сторону треугольника'))
    p = (a1 + a2 + a3)/2
    print(s3(a1,a2,a3,p))
if a == 5:
    R = int(input('введите радиус'))
    print(s4(R))'''

def f(arr):
    total = 0
    for i in arr:
        total += i
    print(total)
    print(total / len(arr))
arr1 = [8,6,3,8,65,89,-74,31]
arr2 = [1,2,3,4,5,6,7,8,9,10]
arr3 = [6,98,3453,0,8,-43534,645,6,4,63,9,100000]
f(arr1)
f(arr2)
f(arr3)

