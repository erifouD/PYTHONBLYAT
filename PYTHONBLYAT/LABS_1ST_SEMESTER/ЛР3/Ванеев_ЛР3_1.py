x=int(input('сторона x='))
y=int(input('сторона y='))
z=int(input('сторона z='))
if z**2+x**2==y**2:
    print('прямоугольный треугольник существует')
    print('площадь S=',0.5*z*x)
elif z**2+y**2==x**2:
    print('прямоугольный треугольник существует')
    print('площадь S=',0.5*z*y)
elif x**2+y**2==z**2:
    print('прямоугольный треугольник существует')
    print('площадь S=',0.5*y*x)
else:
    print('треугольник не существует')
    print('периметр равен',x+y+z)
