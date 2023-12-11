import math
x=float(input('Введите переменную x:'))
y=float(input('Введите переменную y:'))
B=((math.sin(x**3)+(math.cos(x**2)))**3)/(math.pi*abs(2*x*y))
print("B = {0:.2f}".format(B))
print('B =',B)
