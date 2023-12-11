import math

x = abs(float(input("Введите переменную x:")))
y = float(input("Введите переменную y:"))

z = ((math.sqrt(x) + 5 * y) / math.pi + (0.55**3 * math.cos(x)))**3

print('z = {0:.2f}'.format(z))



