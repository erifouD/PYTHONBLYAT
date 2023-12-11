x=int(input('сторона x='))
y=int(input('сторона y='))
z=int(input('сторона z='))
q=0
if z+x>y and z+y>x and x+y>z:
    print('треугольник существует')
    q=0.5*(z+y+x)
    print('площадь S=',round((q*(q-z)*(q-x)*(q-y))**0.5))
else:
    print('NO')

