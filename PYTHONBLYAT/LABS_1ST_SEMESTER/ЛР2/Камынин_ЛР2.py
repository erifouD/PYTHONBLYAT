import math
m = float(input("Введите переменную m: "))
v = float(input("Введите переменную v: "))
z = ((m*(v**2+m))/(3*(math.pi**3-m))+((math.e**m+0.5)+(math.fabs(v-10))/(math.cos(m)-25.8)))

print("z = {0:.2f}".format(z))
