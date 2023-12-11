import math
x = float(input("Введите переменную x"))
t = float(input("Введите переменную t"))
z = ((math.sqrt(math.fabs(x))) + math.sqrt(math.fabs(3*t)**2))/ (math.pi * 0.75) - math.pow(math.e,8)
print("z = {0:.2f}".format(z))


