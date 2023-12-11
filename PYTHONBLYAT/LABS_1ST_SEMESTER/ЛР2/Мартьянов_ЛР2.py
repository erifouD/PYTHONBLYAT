import math
x = int(input('Введите переменную x:'))
y = float(input('Введите переменную у:'))
A = (((abs((math.cos(x))**3))/(3*(math.pi**2)))+(((math.e**(x*y))+abs(x-y))/(y**4)))
print("A = {0:.1f}".format(A))
      
      
