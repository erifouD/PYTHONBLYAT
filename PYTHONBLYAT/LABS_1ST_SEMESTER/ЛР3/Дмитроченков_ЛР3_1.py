from math import sqrt
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

if (a + b > c) and (a + c > b) and (c + b > a):
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Треугольник существует, и его площадь равна ", S)
else:
    print("No")
