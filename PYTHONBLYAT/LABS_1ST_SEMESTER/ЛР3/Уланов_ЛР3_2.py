import math
a=int(input("Введите длину первой стороны:"))
b=int(input("Введите длину второй стороны:"))
c=int(input("Введите длину третьей стороны:"))
if (a+b>c) and (a+c>b) and (b+c>a):
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Треугольник существует, и его площадь равна", S)
else:
        print("NO")
