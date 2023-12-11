import math
a = float(input("Введите переменную x:"))
b = float(input("Введите переменную y:"))

d = (math.pi ** 2) * (math.sqrt(a ** 3 - b ** 3)) - ((math.exp(0.5) + math.log(math.fabs(a * b)))/(0.5 ** 8))
print("d = {0:.2f}".format(d))
