import math
a=float(input('Введите основание треугольника: '))
b=float(input('Введите сторону треугольника:'))
s=(a/4)*math.sqrt(4*b**2-a**2)
if s%2==0:
    print('Площадь треугольника: ', s/2)
else:
    print('Не могу делить на 2!')

