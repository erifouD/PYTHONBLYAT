import math
x=float(input('Введите переменную х:'))
y=float(input('Введите переменную у:'))
z=((x**5 +(math.cos(x**2))**3)/(math.pi *3.57*math.sin(y))) + math.sqrt(x**7 -y**3)
print('z= {0:.2f}'.format(z))
   
