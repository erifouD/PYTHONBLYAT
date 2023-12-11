import math
x=float(input("Введите переменную x:"))
z=float(input("Введите переменную z:"))
y=(math.atan(x+z)/(math.pi*math.sin(z)))+((math.pow(math.e,4*x)/(x*z)))
print("y = {0:.2f}".format(y))
