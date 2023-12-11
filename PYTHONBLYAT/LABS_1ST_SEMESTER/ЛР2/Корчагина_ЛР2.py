import math
x=float(input("Введите переменную x:"))
y=float(input("Введите переменную y:"))
z=(((math.cos(x+y**12))/(math.sqrt(y**3+math.pi-x)))+math.log(x))
print("z={0:.2f}".format(z))

